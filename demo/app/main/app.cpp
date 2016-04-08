//
// Copyright The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//

// WindowTest.cpp: Sample used to test various function of OSWindow

#include <algorithm>
#include <iostream>
#include <Windows.h> 
#include <tchar.h>
int WINAPI wWinMain(HINSTANCE instance,	HINSTANCE prev_instance,wchar_t* /*command_line*/,	int show_command)
//int main(int argc, char *argv[])
{
	::MessageBox(NULL, _T("这是一个Win32的应用"), _T("提示"), 0);
}
