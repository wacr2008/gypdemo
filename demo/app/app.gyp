# Copyright (c) 2010 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{

    'includes': [ '../build/win_precompile.gypi', ],  
      						
    'targets':
    [  
        {
            'target_name': 'app',
            'type': 'executable',
            'dependencies': [  ],
            'includes': [ '../build/common.gypi',
            						],           						
            'sources': [ 'main/app.cpp', 
        								 'main/app.rc',
            						 ],
						'configurations': {
						      'Debug': {
						        'defines': [ 'DEBUG', '_DEBUG' ],
						        'msvs_settings': {
						          'VCCLCompilerTool': {
						            'RuntimeLibrary': 1,  # static debug
						          },
						          'VCLinkerTool': {
											          'GenerateDebugInformation': 'true',
											          'SubSystem': '2',     # Set /SUBSYSTEM:WINDOWS
											},
											'VCManifestTool': {
											          'AdditionalManifestFiles': [
											            'main/app.exe.manifest',
											          ],
											},
						        },
						      },
						      'Release': {
						        'defines': [ 'NDEBUG' ],
						        'msvs_settings': {
						          'VCCLCompilerTool': {
						            'RuntimeLibrary': 0,  # static release
						          },
						          'VCLinkerTool': {
											          'GenerateDebugInformation': 'true',
											          'SubSystem': '2',     # Set /SUBSYSTEM:WINDOWS
											},
											'VCManifestTool': {
											          'AdditionalManifestFiles': [
											            'main/app.exe.manifest',
											          ],
											},
						        },
						      }
						}, 
            'copies':
            [
                {
                    'destination': '<(PRODUCT_DIR)',
                    'files':
                    [
                        'main/basemap.tga',
                        'main/lightmap.tga',
                    ],
                },
            ]
        },
    ],
}
