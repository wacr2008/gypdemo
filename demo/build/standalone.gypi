# Copyright (c) 2014 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        # Assume for the time being that we're never compiling
        # standalone APP on Chrome OS.
        'chromeos': 0,

        # Chromium puts the pkg-config command in a variable because
        # calling pkg-config directly doesn't work in a sysroot image.
        # See Chromium bug 569947 for more information.
        # For standalone builds we don't have this problem so we use
        # the regular command.
        'pkg-config': 'pkg-config',

        # Use a nested variable trick to get use_x11 evaluated more
        # eagerly than other conditional variables.
        'variables':
        {
            'conditions':
            [
                ['OS=="linux"',
                {
                    'use_x11': 1,
                },
                {
                    'use_x11': 0,
                }],
            ],
        },

        # Copy conditionally-set variables out one scope.
        'use_x11%': '<(use_x11)',
    },
}
