# github-2FA-solution
最近github要求2FA配置双重身份验证,我试了各种方法，都觉得不是备份麻烦，就是不安全。于是写了一个python程序解决这个问题
下面是使用方法：
这个程序需要安装pyotp这个运行库，在cmd上输入pip install pyotp安装相应的库
之后用手机上的浏览器之类的软件扫描github提供的二维码，会得到类似于“64WEPLPMZV2N6J6A”之类的base32 编码，
将这个编码粘贴在test_2.py 中的secret_key = ""中，比如secret_key = "64WEPLPMZV2N6J6A"，之后就可以使用了。
