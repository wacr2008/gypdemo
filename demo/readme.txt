提示 提示 提示：
因为此工程使用了python来获取版本号，拷文件等，所以要编绎的话，请先设置环境变量Path，将**\gyp\depot_tools\python276_bin加到环境变量中去。


生成vs工程
python build\gyp_app

编绎app工程
ninja -C out/Debug app

测试版本号
ninja -C out/Debug commit_id