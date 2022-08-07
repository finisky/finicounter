[[中文版](https://github.com/finisky/finicounter#readme)]

# <img src="https://finicounter.vercel.app/logo.png" title="FiniCounter" width="64" align="center"> FiniCounter

[Demo](https://finicounter.vercel.app/en)

[Finisky Garden](https://finisky.github.io/finicounter/en)

![FiniCounter Demo](https://cdn.jsdelivr.net/gh/finisky/finicounter/finicounterdemo.en.png)

## Introduction

FiniCounter is an extremely simple website page views counter for static websites (Hexo/Hugo/Jekyll etc.). When a visitor comes to your website, the page view counter (**not unique visitor**) will increment by 1. The count key is your website's domain name: `example.com`.

FiniCounter is:

* **Totally free**
* **No registration required**

## How to Use

### Basic Usage

1. Add the following script to your websites:

```javascript
<script async src="//finicounter.vercel.app/finicounter.js"></script>
```

2. Add a container with id `finicount_views` to show the view counts:

```html
<span id="finicount_views"></span>
```

You are done! The view count will be shown on your site like this `12,345,678`.

**Notice**: the script should be added to **every** pages of your website. Otherwise, the page view counter might missing counts.

It is also welcome to directly use the counter API `https://finicounter.vercel.app/counter?host=xxx.com` and customize the javascript yourself.

**Each counter will be automatically deleted if not accessed for more than 3 months.**

### Hexo NexT Theme Integration

For Hexo NexT theme, we can easily integrate FiniCounter by [Injects](https://theme-next.js.org/docs/advanced-settings/injects). The total pageview can be displayed in the footer:

![FiniCounter Hexo NexT Demo](https://cdn.jsdelivr.net/gh/finisky/finiskyimages/nextpageviewfooter.png)

Just add a new js file `totalpageview.js` in the Hexo root folder `scripts/`:

```javascript
hexo.extend.filter.register('theme_inject', function(injects) {
  injects.footer.raw('totalpageview', '<div><span><a href="https://finicounter.vercel.app/" target="_blank">Total Pageview:</a></span><span id="finicount_views" style="display:inline;padding-left:5px;"></span><div> <script async src="//finicounter.vercel.app/finicounter.js"></script>', {}, {cache: false});
});
```

Leave Hexo NexT Plugin as future work :-) .


## Known Issues

* Reset Counter: if you want to delete or reset the counter, send me an email (can be found [here](https://finisky.github.io/links/))
* Counter Initialization (todo): each key can be initialized one time within 3 days after creation
