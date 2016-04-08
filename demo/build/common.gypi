# Copyright (c) 2010 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'includes': [ 'common_defines.gypi', ],
    'variables':
    {
        'app_path': '<(DEPTH)',
        'app_build_winrt%': '0',
        'app_build_winphone%': '0',
        'app_build_winrt_app_type_revision%': '8.1',
        'app_build_winrt_target_platform_ver%' : '',
        
        # Use of precompiled headers on Windows.
	      #
	      # This variable may be explicitly set to 1 (enabled) or 0
	      # (disabled) in ~/.gyp/include.gypi or via the GYP command line.
	      # This setting will override the default.
	      #
	      # See
	      # http://code.google.com/p/chromium/wiki/WindowsPrecompiledHeaders
	      # for details.
	      'use_win_pch%': 1,
	      
	     
        
        # app_code is set to 1 for the core APP targets defined in src/build_app.gyp.
        # app_code is set to 0 for test code, sample code, and third party code.
        # When angle_code is 1, we build with additional warning flags on Mac and Linux.
        'app_code%': 0,
        'release_symbols%': 'true',
        'gcc_or_clang_warnings':
        [
            '-Wall',
            '-Wchar-subscripts',
            '-Werror',
            '-Wextra',
            '-Wformat=2',
            '-Winit-self',
            '-Wnon-virtual-dtor',
            '-Wno-format-nonliteral',
            '-Wno-unknown-pragmas',
            '-Wno-unused-function',
            '-Wno-unused-parameter',
            '-Wpacked',
            '-Wpointer-arith',
            '-Wundef',
            '-Wwrite-strings',
        ],

        # TODO: Pull chromium's clang dep.
        'clang%': 0,

        'clang_only_warnings':
        [
            '-Wshorten-64-to-32',
        ],
        
    },
    'target_defaults':
    {
        'default_configuration': 'Debug',
        'variables':
        {
            'warn_as_error%': 0,
        },
        'target_conditions':
        [
            ['warn_as_error == 1',
            {
                'msvs_settings':
                {
                    'VCCLCompilerTool':
                    {
                        'WarnAsError': 'true',
                    },
                    'VCLinkerTool':
                    {
                        'TreatLinkerWarningAsErrors': 'true',
                    },
                },
            }],
        ],
        'conditions':
        [
            ['app_build_winrt==1',
            {
                'msvs_enable_winrt' : '1',
                'msvs_application_type_revision' : '<(app_build_winrt_app_type_revision)',
                'msvs_target_platform_version' : '<(app_build_winrt_target_platform_ver)',
            }],
            ['app_build_winphone==1',
            {
                'msvs_enable_winphone' : '1',
            }],
            
		        #Turn precompiled headers on by default.
		        ['OS=="win" ', {
		          'use_win_pch%': 1
		        }],
        ],
        'configurations':
        {
            'Common_Base':
            {
                'abstract': 1,
                'msvs_configuration_attributes':
                {
                    'OutputDirectory': '$(SolutionDir)$(ConfigurationName)_$(Platform)',
                    'IntermediateDirectory': '$(OutDir)\\obj\\$(ProjectName)',
                    'CharacterSet': '0',    # ASCII
                }, 
		            
                'msvs_settings':
                { 
								    'VCCLCompilerTool': {
	                        # Control Flow Guard is a security feature in Windows
	                        # 8.1 and higher designed to prevent exploitation of
	                        # indirect calls in executables.
	                        # Control Flow Guard is enabled using the /d2guard4
	                        # compiler setting in combination with the /guard:cf
	                        # linker setting.
	                        
	                        'conditions':
					                [
					                    ['MSVS_VERSION=="2008"' ,
					                    { 
					                        'AdditionalOptions': ['/MP',],
					                    },
					                    {
					                        'AdditionalOptions': ['/MP', '/d2guard4'],
					                    }],
					                ],
							            'BufferSecurityCheck': 'true',
	                        'DebugInformationFormat': '3',
	                        'ExceptionHandling': '0',
	                        'EnableFunctionLevelLinking': 'true',
	                        'MinimalRebuild': 'false',
	                        'WarningLevel': '4',
	                  }, 
										
										 
                    'VCLinkerTool':
                    {
                        # Control Flow Guard is a security feature in Windows
                        # 8.1 and higher designed to prevent exploitation of
                        # indirect calls in executables.
                        # Control Flow Guard is enabled using the /d2guard4
                        # compiler setting in combination with the /guard:cf
                        # linker setting.
                        'AdditionalOptions': ['/guard:cf'],
                        'FixedBaseAddress': '1',
                        'ImportLibrary': '$(OutDir)\\lib\\$(TargetName).lib',
                        'MapFileName': '$(OutDir)\\$(TargetName).map',
                        # Most of the executables we'll ever create are tests
                        # and utilities with console output.
                        'SubSystem': '1',    # /SUBSYSTEM:CONSOLE
                    },
                    'VCResourceCompilerTool':
                    {
                        'Culture': '1033',
                    },
                },
                'xcode_settings':
                {
                    'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
                },
            },    # Common_Base

            'Debug_Base':
            {
                'abstract': 1,
                'defines':
                [
                    '_DEBUG'
                ],
                'msvs_settings':
                {
                    'VCCLCompilerTool':
                    {
                        'Optimization': '0',    # /Od
                        'BasicRuntimeChecks': '3',
                        'RuntimeTypeInfo': 'true',
                        'conditions':
                        [
                            ['app_build_winrt==1',
                            {
                                # Use the dynamic C runtime to match
                                # Windows Application Store requirements

                                # The C runtime for Windows Store applications
                                # is a framework package that is managed by
                                # the Windows deployment model and can be
                                # shared by multiple packages.

                                'RuntimeLibrary': '3', # /MDd (debug dll)
                            },
                            {
                                # Use the static C runtime to
                                # match chromium and make sure
                                # we don't depend on the dynamic
                                # runtime's shared heaps
                                'RuntimeLibrary': '1', # /MTd (debug static)
                            }],
                        ],
                    },
                    'VCLinkerTool':
                    {
                        'GenerateDebugInformation': 'true',
                        'LinkIncremental': '2',
                        'conditions':
                        [
                            ['app_build_winrt==1',
                            {
                                'AdditionalDependencies':
                                [
                                    'dxgi.lib',
                                ],
                                'EnableCOMDATFolding': '1', # disable
                                'OptimizeReferences': '1', # disable
                            }],
                        ],
                    },
                },
                'xcode_settings':
                {
                    'COPY_PHASE_STRIP': 'NO',
                    'GCC_OPTIMIZATION_LEVEL': '0',
                },
            },    # Debug_Base

            'Release_Base':
            {
                'abstract': 1,
                'defines':
                [
                    'NDEBUG'
                ],
                'msvs_settings':
                {
                    'VCCLCompilerTool':
                    {
                        'RuntimeTypeInfo': 'false',

                        'conditions':
                        [
                            ['app_build_winrt==1',
                            {
                                # Use Chromium's settings for 'Official' builds
                                # to optimize WinRT release builds
                                'Optimization': '1', # /O1, minimize size
                                'FavorSizeOrSpeed': '2', # /Os
                                'WholeProgramOptimization': 'true',

                                # Use the dynamic C runtime to match
                                # Windows Application Store requirements

                                # The C runtime for Windows Store applications
                                # is a framework package that is managed by
                                # the Windows deployment model and can be
                                # shared by multiple packages.
                                'RuntimeLibrary': '2', # /MD (nondebug dll)
                            },
                            {
                                'Optimization': '2', # /O2, maximize speed

                                # Use the static C runtime to
                                # match chromium and make sure
                                # we don't depend on the dynamic
                                'RuntimeLibrary': '0', # /MT (nondebug static)
                            }],
                        ],
                    },
                    'VCLinkerTool':
                    {
                        'GenerateDebugInformation': '<(release_symbols)',
                        'LinkIncremental': '1',

                        'conditions':
                        [
                            ['app_build_winrt==1',
                            {
                                # Use Chromium's settings for 'Official' builds
                                # to optimize WinRT release builds
                                'LinkTimeCodeGeneration': '1',
                                'AdditionalOptions': ['/cgthreads:8'],
                            }],
                        ],
                    },
                },
            },    # Release_Base

            'x86_Base':
            {
                'abstract': 1,
                'msvs_configuration_platform': 'Win32',
                'msvs_settings':
                {
                    'VCLinkerTool':
                    {
                        'TargetMachine': '1', # x86
                    },
                    'VCLibrarianTool':
                    {
                        'TargetMachine': '1', # x86
                    },
                },
            }, # x86_Base

            'x64_Base':
            {
                'abstract': 1,
                'msvs_configuration_platform': 'x64',
                'msvs_settings':
                {
                    'VCLinkerTool':
                    {
                        'TargetMachine': '17', # x86 - 64
                    },
                    'VCLibrarianTool':
                    {
                        'TargetMachine': '17', # x86 - 64
                    },
                },
            },    # x64_Base

            # Concrete configurations
            'Debug':
            {
                'inherit_from': ['Common_Base', 'x86_Base', 'Debug_Base'],
            },
            'Release':
            {
                'inherit_from': ['Common_Base', 'x86_Base', 'Release_Base'],
            },
            'conditions':
            [
                ['app_build_winrt==0 and OS == "win" and MSVS_VERSION != "2010e"',
                {
                    'Debug_x64':
                    {
                        'inherit_from': ['Common_Base', 'x64_Base', 'Debug_Base'],
                    },
                    'Release_x64':
                    {
                        'inherit_from': ['Common_Base', 'x64_Base', 'Release_Base'],
                    },
                }],
                ['app_build_winrt==1',
                {
                    'arm_Base':
                    {
                        'abstract': 1,
                        'msvs_configuration_platform': 'ARM',
                        'msvs_settings':
                        {
                            'VCLinkerTool':
                            {
                                'TargetMachine': '3', # ARM
                            },
                            'VCLibrarianTool':
                            {
                                'TargetMachine': '3', # ARM
                            },
                        },
                    }, # arm_Base
                }],
                ['app_build_winrt==1 and app_build_winphone==0',
                {
                    'Debug_x64':
                    {
                        'inherit_from': ['Common_Base', 'x64_Base', 'Debug_Base'],
                    },
                    'Release_x64':
                    {
                        'inherit_from': ['Common_Base', 'x64_Base', 'Release_Base'],
                    },
                    'Debug_ARM':
                    {
                        'inherit_from': ['Common_Base', 'arm_Base', 'Debug_Base'],
                    },
                    'Release_ARM':
                    {
                        'inherit_from': ['Common_Base', 'arm_Base', 'Release_Base'],
                    },
                }],
                ['app_build_winrt==1 and app_build_winphone==1',
                {
                    'Debug_ARM':
                    {
                        'inherit_from': ['Common_Base', 'arm_Base', 'Debug_Base'],
                    },
                    'Release_ARM':
                    {
                        'inherit_from': ['Common_Base', 'arm_Base', 'Release_Base'],
                    },
                }],
            ],
        },    # configurations
    },    # target_defaults
    'conditions':
    [
        ['OS == "win"',
        {
            'target_defaults':
            {
                'msvs_cygwin_dirs': ['../third_party/cygwin'],
            },
        },
        { # OS != win
            'target_defaults':
            {
                'cflags':
                [
                    '-fPIC',
                ],
                'cflags_cc':
                [
                    '-std=c++0x',
                ],
            },
        }],
        ['OS != "win" and OS != "mac"',
        {
            'target_defaults':
            {
                'cflags':
                [
                    '-pthread',
                ],
                'cflags_cc':
                [
                    '-fno-exceptions',
                ],
                'ldflags':
                [
                    '-pthread',
                ],
                'configurations':
                {
                    'Debug':
                    {
                        'variables':
                        {
                            'debug_optimize%': '0',
                        },
                        'defines':
                        [
                            '_DEBUG',
                        ],
                        'cflags':
                        [
                            '-O>(debug_optimize)',
                            '-g',
                        ],
                    }
                },
            },
        }],
        ['app_code==1',
        {
            'target_defaults':
            {
                'conditions':
                [
                    ['OS == "mac"',
                    {
                        'xcode_settings':
                        {
                            'WARNING_CFLAGS': ['<@(gcc_or_clang_warnings)']
                        },
                    }],
                    ['OS != "win" and OS != "mac"',
                    {
                        'cflags': ['<@(gcc_or_clang_warnings)']
                    }],
                    ['clang==1',
                    {
                        'cflags': ['<@(clang_only_warnings)']
                    }],
                ]
            }
        }],
    ],
}
