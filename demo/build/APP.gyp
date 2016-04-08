# Copyright (c) 2010 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'targets':
    [
        {
            'target_name': 'All',
            'type': 'none',
            'dependencies':
            [
                '../src/app.gyp:*',
            ],
            'conditions':
            [
                # Don't generate samples for WinRT
                ['app_build_winrt==0',
                {
                    'dependencies':
                    [
                        '../app/app.gyp:*',
                    ],
                }],
            ],
        },
    ],
}
