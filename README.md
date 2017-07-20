
settings.py 中需要填充所需信息:
<pre><code> PASS
</code></pre>

包依赖
=============
  1 selenium
  2 [wxpy](https://github.com/youfou/wxpy "Title")  一款优雅微信个人号,安装方法:
 <pre><code>pip install -U wxpy
</code></pre>


env
=============
 1. 环境当前兼容 mac
  2. 当前使用的fireFox 浏览器,确保你有该浏览器<且新版>
  3. fireFox 驱动, 我在目录已存有一份当前可用geckodriver
  4. 请给 Driver添加执行权限 ->
  <pre><code>sudo chmod u+x geckodriver
</code></pre>
  5. 目前仅兼容python2.7+ 其他版本请自行根据错误提示替换代码


How TO USE:
=============
  1. 需要你有一个微信号
  2. 建议是启动一个新的窗口<mac 多窗口>
  3. 终端执行:
  <pre><code>python sendCode.py  </code></pre>
  4. 改命令执行后出现的终端二维码, 请微信扫描登录
    **Login successfully as xxx**则代表登录成功

签入 & 签出:
=============
  发送 **CheckOut**<无所谓大小写>  -> 签出
  发送 **CheckIn**<无所谓大小写>   -> 签入


Roses are red
Violets are blue


