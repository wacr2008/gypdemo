# Copyright (c) 2013 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        'app_standalone%': 0,

        # These file lists are shared with the GN build.
        
        'libapp_includes':
        [
            '../include/export.h',
        ],
        'libapp_sources':
        [ 
            'third_party/murmurhash/MurmurHash3.cpp',
            'third_party/murmurhash/MurmurHash3.h',
        ],  
        'libapp_d3d9_sources':
        [ 
           
        ],              
        'libCommon_sources':
        [ 
            'libCommon/libCommon.cpp',
            'libCommon/libCommon.def',
            'libCommon/libCommon.rc',
            'libCommon/resource.h',
        ], 
    },
    # Everything below this is duplicated in the GN build. If you change
    # anything also change angle/BUILD.gn
    'targets':
    [
        {
            'target_name': 'libAPP',
            'type': 'static_library',
            'dependencies':
            [
                'commit_id',
            ],
            'includes': [ '../build/common_defines.gypi', ],
            'include_dirs':
            [
                '.',
                '../include',
                'third_party/khronos',
            ],
            'sources':
            [
                '<@(libapp_sources)',
                '<@(libapp_includes)',
            ],
            'defines':
            [
                'LIB_APP_IMPLEMENTATION',
            ],
            'direct_dependent_settings':
            {
                'include_dirs':
                [
                    '<(app_path)/src',
                    '<(app_path)/include',
                ],
                'defines':
                [
                    'GL_GLEXT_PROTOTYPES',
                    'ANGLE_PRELOADED_D3DCOMPILER_MODULE_NAMES={ "d3dcompiler_47.dll", "d3dcompiler_46.dll", "d3dcompiler_43.dll" }',
                ],
                'conditions':
                [
                    ['OS=="win"', {
                        'defines':
                        [
                            'GL_APICALL=',
                            'EGLAPI=',
                        ],
                    }, {
                        'defines':
                        [
                            'GL_APICALL=__attribute__((visibility("default")))',
                            'EGLAPI=__attribute__((visibility("default")))',
                        ],
                    }],
                    ['OS == "mac"',
                    {
                        'xcode_settings':
                        {
                            'DYLIB_INSTALL_NAME_BASE': '@rpath',
                        },
                    }],
                    ['app_enable_d3d9==1',
                    {
                        'defines':
                        [
                            'APP_ENABLE_D3D9',
                        ],
                    }],
                    ['app_enable_d3d11==1',
                    {
                        'defines':
                        [
                            'APP_ENABLE_D3D11',
                        ],
                    }], 
                ],
            },
            'conditions':
            [ 
                ['app_enable_d3d9==1',
                {
                    'sources':
                    [
                        '<@(libapp_d3d9_sources)',
                    ],
                    'defines':
                    [
                        'APP_ENABLE_D3D9',
                    ],
                    'link_settings':
                    {
                        'msvs_settings':
                        {
                           'VCCLCompilerTool':
			                     {
			                        'WarnAsError': 'false',
			                     },
                            'VCLinkerTool':
                            {
                                'conditions':
                                [
                                    ['app_build_winrt==0',
                                    {
                                        'AdditionalDependencies':
                                        [
                                            'dxguid.lib',
                                            'd3d9.lib',
                                        ],
                                    }],
                                    ['app_build_winrt==1',
                                    {
                                        'AdditionalDependencies':
                                        [
                                            'dxguid.lib',
                                            'd3d9.lib',
                                        ],
                                    }],
                                ], 
                            }
                        },
                    },
                }], 
                ['app_build_winrt==0 and OS=="win"',
                {
                    'dependencies':
                    [
                        'copy_compiler_dll'
                    ],
                }],
                ['app_build_winrt==1',
                {
                    'msvs_requires_importlibrary' : 'true',
                }],
            ],
        },
        {
            'target_name': 'libCommon',
            'type': '<(app_library_type)',
            'dependencies': [ 'libAPP'],
            'includes': [ '../build/common_defines.gypi', ],
            'sources':
            [
                '<@(libCommon_sources)',
            ],
            'defines':
            [
                'LIB_COMMON_IMPLEMENTATION',
            ],
            'conditions':
            [
                ['app_build_winrt==1',
                {
                    'msvs_requires_importlibrary' : 'true',
                }],
                ['app_build_winphone==1',
                {
                    'msvs_enable_winphone' : '1',
                }],
            ],
        },
    ],
}
