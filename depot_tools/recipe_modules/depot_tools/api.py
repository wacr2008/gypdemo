# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from recipe_engine import recipe_api

class DepotToolsApi(recipe_api.RecipeApi):
  @property
  def download_from_google_storage_path(self):
    return self.package_repo_resource('download_from_google_storage.py')

  @property
  def ninja_path(self):
    ninja_exe = 'ninja.exe' if self.m.platform.is_win else 'ninja'
    return self.package_repo_resource(ninja_exe)
