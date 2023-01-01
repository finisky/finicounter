[[English](https://github.com/finisky/finicounter/blob/master/README.en.md)]

# <img src="https://finicounter.eu.org/logo.png" title="FiniCounter" width="64" align="center"> FiniCounter

[Demo网站](https://finicounter.eu.org/)

[Finisky Garden](https://finisky.eu.org/finicounter)

![FiniCounter Demo](https://raw.githubusercontent.com/finisky/finicounter/master/finicounterdemo.png)

## 简介

FiniCounter是一个极简网站访客计数器，适用于各种静态网站的全站访客数统计 (如 Hexo/Hugo/Jekyll 等生成的静态站)。每当有用户访问了该网站的任意页面，网站访问量加1 (**非UV，同一用户刷新页面两次会计数2**)。进行统计的key为该网站的域名，如 `example.com`，而非 `example.com/path`。

FiniCounter:

* **完全免费**
* **无需注册**


## 如何使用
### 基本用法

1. 添加一行javascript到网页：

```javascript
<script async src="//finicounter.eu.org/finicounter.js"></script>
```

2. 添加任意容器来显示访客数，id 必须为 `finicount_views` :

```html
<span id="finicount_views"></span>
```

搞定！访客数已经可以在你的网站中显示了，就像这样：`12,345,678` 。

**注意**: 上面的javascript需要在网站的**每个页面**都添加 (无需都显示)，否则计数器可能会丢失这些未添加页面的访问计数。

如有必要，也可直接使用这里的计数API `https://finicounter.eu.org/counter?host=xxx.com`，自行定制对应的javascript进行计数展示。

**如果某网站计数三个月没有修改，则计数会被自动清除。**

### Hexo NexT集成

如果使用NexT主题，可采用 [Injects](https://theme-next.js.org/docs/advanced-settings/injects) 的方法进行集成，将网站访问数显示在页脚：

![FiniCounter Hexo NexT Demo](https://cdn.jsdelivr.net/gh/finisky/finiskyimages/nextpageviewfooter.png)

在Hexo根目录的 `scripts/` 中添加新文件 `totalpageview.js` 即可:

```javascript
hexo.extend.filter.register('theme_inject', function(injects) {
  injects.footer.raw('totalpageview', '<div><span><a href="https://finicounter.eu.org/" target="_blank">Total Pageview:</a></span><span id="finicount_views" style="display:inline;padding-left:5px;"></span><div> <script async src="//finicounter.eu.org/finicounter.js"></script>', {}, {cache: false});
});
```

如果受欢迎，可以开发一个Hexo NexT Plugin进一步简化集成操作 :-) 。


## 已知问题

* 重置计数器：如希望删除或重置计数器，可在这里提 Issue 或发邮件 (邮件在 [这里](https://finisky.eu.org/links/))。
* 初始化计数器 (todo)：每个key可在第一次被创建后的3天内初始化一次。
