# learnPythonCrawler

## Resources

- https://zhuanlan.zhihu.com/p/25250739
- https://juejin.im/post/58885a651b69e6005930ba8b
- http://cuiqingcai.com/1052.html

### [Python爬虫进阶三之Scrapy框架安装配置](http://cuiqingcai.com/912.html)

在这一节中，我直接跳过 windows 平台安装的部分，看的是 Linux Unbuntu 平台安装的部分。 python2.7 是默认在我的 mac 上安装好的，pip 通过在 item2 中输入 pip 命令也可以直接看到是安装好了的。 lxml 没有安装，通过 sudo pip install lxml 实现安装。 openssl 也是通过输入 openssl 命令看到是安装好的。 但是在安装 scrapy 的过程总却报错了，安装完后，敲入 scrapy 命令回车，报错 ImportError: cannot import name xmlrpc_client 的错误。好像是和 six 这个模块有关系。通过 google，找到了一个 SO 的[解决方案](http://stackoverflow.com/questions/30964836/scrapy-throws-importerror-cannot-import-name-xmlrpc-client)。这个问答中通过执行 Dan Banks 的回答实现了 scrapy 的安装。即首先执行 `sudo pip uninstall six`，然后执行 `sudo easy_install six`。之后再打入 `scrapy` 命令就 ok 了。

### 本仓库中关于 qsbk.py

qsbk.py 这个文件是照着[Python爬虫实战一之爬取糗事百科段子](http://cuiqingcai.com/990.html)这篇文章来做的实践。这里面需要注意下面几个问题。第一，访问糗事百科必须要设置 headers 才可以访问，这个 headers 设置中必须要设置 User-Agent 这个属性，这个属性你可以通过浏览器访问糗事百科官网，然后查看 network 这部分的内容得到。其次要匹配的内容必须要 decode("utf-8") 才可以。就是 `response.read().decode("utf-8")` 才可以。然后就是最麻烦的正则了，正则的话楼主也讲了几个常见的用法，比如 `.*?`，还有 `(.*?)`，还有 re.S 表示 `.` 匹配任意模式，包括换行符（正常情况下 `.` 不能匹配换行符 `\n`）。这里面我主要说下 `(.*?)`，楼主的解释我一直没有看明白，后来自己写代码才知道 `(.*?)` 表示所有的内容，比如我的代码中只有一个 `(.*?)`，那么 item 就只有一个元素， item[0]，这个就表示两个 `<span>` 和 `</span>` 之间的所有内容。所以 print item[0] 的时候就会打印这个 `span` 元素中的内容，也就是糗百每个段子的实际内容。因为楼主的正则比较复杂，我这里就不具体分析了，所以楼主后面还验证了 item[3] 中是否含有 img 元素，如果有的话就跳过打印 item[3]

### [Python爬虫利器二之Beautiful Soup的用法](http://cuiqingcai.com/1319.html)

这篇博客中，需要安装 beautifulsoup4, lxml 和 html5lib 三个包。安装 beautifulsoup 过程中会出现一些错误，后来我先用 sudo pip uninstall beautifulsoup4 这个命令卸载了 beautifulsoup4，然后通过 sudo easy_install beautifulsoup4 重新安装成功了。在安装 html5lib 的过程中报错 `html5lib requires setuptools version 18.5 or above; please upgrade before installing`，后来通过 google 在 SO 上找到了一个[解决方案](http://stackoverflow.com/questions/39162033/html5lib-requires-setuptools-version-18-5-or-above-please-upgrade-before-instal)，由 gonz 回答的方法，就是首先要通过 `sudo pip install -U setuptools` 升级 setuptools。

### [Python爬虫进阶二之PySpider框架安装配置](http://cuiqingcai.com/2443.html)

这篇博客中，需要安装 phantomjs，根据博主的说明，应该使用 `brew install phantomjs` 这个命令。不过我输入这个命令之后，显示 `brew: command not found`。找到 [Homebrew](https://brew.sh/) 的官网，然后根据官网的说明，在命令行输入 /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 下载并安装 brew。安装成功之后，就可以执行 `brew install phantomjs` 命令了。

在安装 pyspider 的时候，根据博主的说明，输入 `pip install pyspider` 命令，出现一个报错，大概是说一个 __call__() 函数需要两个参数，而只提供了一个参数，所以无法执行，在网上搜了一下，发现是 pip 的一个 bug，根据 [stackoverflow](http://stackoverflow.com/questions/42029545/pip-is-error-typeerror-call-takes-exactly-2-arguments-1-given) 上 李思聪 的回答，执行 `sudo python -m pip install --upgrade --force pip` 命令，对 pip 进行了强制升级（好像是这个意思）。然后再执行 `sudo pip install setuptools==33.1.1` 命令。然后再执行 `pip install pyspider`，结果发现在公司总是报一个 httpsconnectionpool(host='pypi.python.org' port=443) read timed out 的错误，后来又 google，发现是 pip 安装包的时候不允许使用代理，可能是因为公司网络使用代理的原因，所以无法下载安装，后来就把电脑带回家，结果执行命令之后就安装好了。

安装好之后，执行 `pyspider all` 结果发现还是报错。目前进行到这一步已经进行不下去了，报错是 pycurl 版本的问题，尝试了各种方法也不行。还有一个报错也解决不了，就是 no module named xmlrpc_server。

--目前这个仓库的内容暂停更新--

### 关于 pyspider 和 scrapy 的比较

这篇[中文的博客](http://f.dataguru.cn/thread-715820-1-1.html)讲的不错，用 google 搜错 pyspider vs scrapy 也可以看到很多英文的分析。可以去详细了解一下。


---目前关于这个问题的答案收集---

http://blog.csdn.net/webstudy8/article/details/51626395