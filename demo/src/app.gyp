# Copyright (c) 2012 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        'app_code': 1,
        'app_post_build_script%': 0,
        'app_gen_path': '<(SHARED_INTERMEDIATE_DIR)/app',
        'app_id_script_base': 'commit_id.py',
        'app_id_script': '<(app_gen_path)/<(app_id_script_base)',
        'app_id_header_base': 'commit.h',
        'app_id_header': '<(app_gen_path)/id/<(app_id_header_base)',
        'app_use_commit_id%': '<!(python <(app_id_script_base) check ..)',
        'app_enable_d3d9': 1,
        'app_enable_d3d11': 1, 
        'app_library_type%': 'shared_library',
        'conditions':
        [
            ['OS=="win"',
            {
                'app_enable_d3d9%': 1,
                'app_enable_d3d11%': 1,
            }],  
        ],
    },
    'includes':
    [ 
        'libCommon.gypi'
    ],

    'targets':
    [
         
        {
            'target_name': 'copy_scripts',
            'type': 'none',
            'includes': [ '../build/common_defines.gypi', ],
            'hard_dependency': 1,
            'copies':
            [
                {
                    'destination': '<(app_gen_path)',
                    'files': [ 'copy_compiler_dll.bat', '<(app_id_script_base)' ],
                },
            ],
            'conditions':
            [
                ['app_build_winrt==1',
                {
                    'type' : 'shared_library',
                }],
            ],
        },
    ],
    'conditions':
    [
        ['app_use_commit_id!=0',
        {
            'targets':
            [
                {
                    'target_name': 'commit_id',
                    'type': 'none',
                    'includes': [ '../build/common_defines.gypi', ],
                    'dependencies': [ 'copy_scripts', ],
                    'hard_dependency': 1,
                    'actions':
                    [
                        {
                            'action_name': 'Generate APP Commit ID Header',
                            'message': 'Generating APP Commit ID',
                            # reference the git index as an input, so we rebuild on changes to the index
                            #'inputs': [ '<(app_id_script)', '<(app_path)/.git/index' ],
                            'inputs': [ '<(app_id_script)', '<(app_path)/svncheck/index' ],
                            'outputs': [ '<(app_id_header)' ],
                            'msvs_cygwin_shell': 0,
                            'action':
                            [
                                'python', '<(app_id_script)', 'gen', '<(app_path)', '<(app_id_header)'
                            ],
                        },
                    ],
                    'all_dependent_settings':
                    {
                        'include_dirs':
                        [
                            '<(app_gen_path)',
                        ],
                    },
                    'conditions':
                    [
                        ['app_build_winrt==1',
                        {
                            'type' : 'shared_library',
                        }],
                    ],
                }
            ]
        },
        { # app_use_commit_id==0
            'targets':
            [
                {
                    'target_name': 'commit_id',
                    'type': 'none',
                    'hard_dependency': 1,
                    'includes': [ '../build/common_defines.gypi', ],
                    'copies':
                    [
                        {
                            'destination': '<(app_gen_path)/id',
                            'files': [ '<(app_id_header_base)' ]
                        }
                    ],
                    'all_dependent_settings':
                    {
                        'include_dirs':
                        [
                            '<(app_gen_path)',
                        ],
                    },
                    'conditions':
                    [
                        ['app_build_winrt==1',
                        {
                            'type' : 'shared_library',
                        }],
                    ],
                }
            ]
        }],
        ['OS=="win"',
        {
            'targets':
            [
                {
                    'target_name': 'copy_compiler_dll',
                    'type': 'none',
                    'dependencies': [ 'copy_scripts', ],
                    'includes': [ '../build/common_defines.gypi', ],
                    'conditions':
                    [
                        ['app_build_winrt==0',
                        {
                            'actions':
                            [
                                {
                                    'action_name': 'copy_dll',
                                    'message': 'Copying D3D Compiler DLL...',
                                    'msvs_cygwin_shell': 0,
                                    'inputs': [ 'copy_compiler_dll.bat' ],
                                    'outputs': [ '<(PRODUCT_DIR)/d3dcompiler_47.dll' ],
                                    'action':
                                    [
                                        "<(app_gen_path)/copy_compiler_dll.bat",
                                        "$(PlatformName)",
                                        "<(windows_sdk_path)",
                                        "<(PRODUCT_DIR)"
                                    ],
                                },
                            ], #actions
                        }],
                        ['app_build_winrt==1',
                        {
                            'type' : 'shared_library',
                        }],
                    ]
                },
            ], # targets
        }],
        ['app_post_build_script!=0 and OS=="win"',
        {
            'targets':
            [
                {
                    'target_name': 'post_build',
                    'type': 'none',
                    'includes': [ '../build/common_defines.gypi', ],
                    'dependencies': [ 'libCommon'],
                    'actions':
                    [
                        {
                            'action_name': 'APP Post-Build Script',
                            'message': 'Running <(app_post_build_script)...',
                            'msvs_cygwin_shell': 0,
                            'inputs': [ '<(app_post_build_script)', '<!@(["python", "<(app_post_build_script)", "inputs", "<(app_path)", "<(CONFIGURATION_NAME)", "$(PlatformName)", "<(PRODUCT_DIR)"])' ],
                            'outputs': [ '<!@(python <(app_post_build_script) outputs "<(app_path)" "<(CONFIGURATION_NAME)" "$(PlatformName)" "<(PRODUCT_DIR)")' ],
                            'action': ['python', '<(app_post_build_script)', 'run', '<(app_path)', '<(CONFIGURATION_NAME)', '$(PlatformName)', '<(PRODUCT_DIR)'],
                        },
                    ], #actions
                },
            ], # targets
        }],
    ] # conditions
}
