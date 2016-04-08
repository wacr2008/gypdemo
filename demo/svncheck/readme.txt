对于git来说，需要以下两个操作：
1.打开 src/commit_id.py中的
index_path = os.path.join(cwd, '.git', 'index')
注释掉index_path = os.path.join(cwd, 'svncheck', 'index')
2.打开src/app.gyp
'inputs': [ '<(app_id_script)', '<(app_path)/.git/index' ],
注释掉'inputs': [ '<(app_id_script)', '<(app_path)/svncheck/index' ],

因为目前我这里使用svn，所以只能将git改为pysvn来获取版本号了
