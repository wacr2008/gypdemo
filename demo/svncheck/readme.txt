����git��˵����Ҫ��������������
1.�� src/commit_id.py�е�
index_path = os.path.join(cwd, '.git', 'index')
ע�͵�index_path = os.path.join(cwd, 'svncheck', 'index')
2.��src/app.gyp
'inputs': [ '<(app_id_script)', '<(app_path)/.git/index' ],
ע�͵�'inputs': [ '<(app_id_script)', '<(app_path)/svncheck/index' ],

��ΪĿǰ������ʹ��svn������ֻ�ܽ�git��Ϊpysvn����ȡ�汾����
