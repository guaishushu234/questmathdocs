# 参与文档编写

以下大部分内容改编自 OI-Wiki 的 [编写指南](https://oi-wiki.org/intro/htc/)，感谢前辈的付出与试验！

## 在 GitHub 上编辑（请仔细阅读本节）

参与 QuestMath Tutoring Hub 的编写 **需要** 一个 GitHub 账号（可以前往 [GitHub 的账号注册页面](https://github.com/signup) 页面注册），但 **不需要** 高超的 GitHub 技巧，即使你是一名新手，只要按照下面所述的步骤操作，也能够 **非常出色** 地完成编辑。

!!! warning Tips
    在你的更改被合并到 QuestMath Tutoring Hub 的主仓库之前，你对 QuestMath Tutoring Hub 的内容所作出的修改均不会出现在 QuestMath Tutoring Hub 的主站上，所以无需担心你的修改会破坏 QuestMath Tutoring Hub 上正在显示的内容。
    
    如果还是不放心，可以查看 [GitHub 的官方教程](https://skills.github.com/)。

### 编辑单个页面内的内容

1.  在 QuestMath Tutoring Hub 上找到对应页面；
2.  点击正文右上方（目录左侧）的 **「编辑此页」**（<i class="md-icon">edit</i>）按钮，跳转到 GitHub 进行编辑；
3.  在编辑框内编写你想修改的内容。请注意，在修改和接下来的提交过程中，请 **关闭您的自动翻译软件**，因为它可能产生不必要的麻烦（例如您修改的文件有时会被其错误改名，从而影响目录结构）；
4.  编写完成后滚动到页面下方，按照本文中 [commit 信息格式规范](#commit-) 填写 commit 信息，之后点击 **Propose changes** 按钮提交修改。点击按钮后，GitHub 会自动帮你创建一份 QuestMath Tutoring Hub 仓库的分支，并将你的提交添加到这个分支仓库。
5.  GitHub 会自动跳转到你的分支仓库的页面，此时页面上方会显示一个绿色的 **Create pull request** 按钮，点击后 GitHub 会跳转到一个创建 Pull Request 页面。向下滚动检查自己所作出的修改没有错误后，按照本文中 [Pull Request 信息格式规范](##pull-request-) 一节中的规范书写 Pull Request 信息，然后点击页面上的绿色的 **Create pull request** 按钮创建 Pull Request。
6.  不出意外的话，你的 Pull Request 就顺利提交到仓库，等待管理员审核并合并到主仓库中即可。

在等待合并的时间里，你可以给他人的 Pull Request 提意见、点赞或者点踩。如果有新消息，会在网页右上角出现提示，并附有邮件提醒（取决于个人设置中配置的通知方式）。

### 编辑多个页面内的内容

如果你需要同时编辑互相无关联的多个页面的内容，请按照上方的 [编辑单个页面内的内容](#编辑单个页面内的内容) 一节一次修改所有页面。

1.  打开 [QuestMath Tutoring Hub](https://github.com/frontecho/questmathdocs) 仓库，点击键盘上的<kbd>.</kbd>按钮（或者将 URL 中的 `github.com` 更改为 `github.dev`），进入 GitHub 的网页版 VS Code 编辑器；
2.  在编辑器中作出对页面源文件的更改，可以使用页面右上方的预览按钮（或按下<kbd>Ctrl+K</kbd><kbd>V</kbd>快捷键）在右侧打开预览界面；
3.  修改完成后使用左侧的 Source Control 选项卡，并按照本文中 [commit 信息格式规范](#commit-) 填写 commit 信息并提交，提交时会提示是否创建此仓库的分支，点击绿色的 **Fork Repository** 按钮即可。
4.  提交后会在网页上方的中央弹出一个提示框，在第一次的提示框内填写标题，第二次的提示框内填写此提交要提交到的仓库内分支名称，之后右下角会弹出一个提示框，内容类似于 `Created Pull Request #1 for frontecho/questmathdocs.`，点击蓝字链接即可查看该 Pull Request。

### 向 Pull Request 追加更改

1.  打开 [QuestMath Tutoring Hub 的 Pull Request 列表](https://github.com/frontecho/questmathdocs/pulls)，找到您提交的 Pull Request 并点击。
2.  Pull Request 页面的标题下方将会有一段例如 `<您的ID> wants to merge x commits into questmathdocs:master from <您的ID>:patch-1` 的文字，点击 `<您的ID>:patch-1` 部分。
3.  您应该会被重定向到您的分支仓库中，而且文件列表左上角的分支名称是你提交 Pull Request 的分支名称（在本示例中应为 `patch-1`）。
4.  进行您需要的更改。
    -   如果您需要编辑单个文件或多个互相无关联的页面的内容，请直接找到你要的文件并进行更改，更改完成后滚动到页面下方，按照本文中 [commit 信息格式规范](#commit-信息格式规范) 填写 commit 信息，之后点击 **Commit changes** 按钮提交修改。
    -   如果您需要编辑多个文件，点击键盘上的<kbd>.</kbd>按钮（或者将 URL 中的 `github.com` 更改为 `github.dev`），进入 GitHub 的网页版 VS Code 编辑器并作出更改。然后使用左侧的 Source Control 选项卡，并按照本文中 [commit 信息格式规范](#commit-信息格式规范) 填写 commit 信息并提交修改。
5.  这时你的更改会被自动追加在您的 Pull Request 中。

### 对于目录和引用的变更

通常情况下，如果您需要添加一个新页面，或者修改已有页面在目录中的链接，您就需要对 [`mkdocs.yml`](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) 文件作出改动。

添加新页面可以参考既有的格式。但除非是进行重构或修正名词，否则 **我们不建议对既有页面的引用链接进行修改**，Pull Requests 中不必要的修改也将被驳回。

## 使用 Git 在本地进行编辑
!!! warning
    对于一般用户，我们更推荐使用上方所述的 GitHub 的 Web 编辑器进行编辑。

虽然大多数情况下您可以直接在 GitHub 上进行编辑，但对于一些较为特殊的情况（如需要使用 GPG 签名），我们更推荐使用 Git 在本地进行编辑。

大致流程如下：

1.  将主仓库 Fork 到自己的仓库中；
2.  将 Fork 后的分支仓库克隆（clone）到本地；
3.  在本地进行修改后提交（commit）这些更改；
4.  将这些更改推送（push）到你克隆的分支仓库；
5.  提交 Pull Request 至主仓库。

### 向 Pull Request 追加更改

在 clone 下来的本地分支仓库中继续进行修改，并提交（commit）以及推送（push）这些更改即可。你的更改会被自动追加在 Pull Request 中。


## Git & GitHub 基本使用方法与团队协作开发

### 学习使用 Git & GitHub

[（官方）GitHub Skills](https://skills.github.com/)

[（视频）【GeekHour】一小时Git教程](https://www.bilibili.com/video/BV1HM411377j/)

### commit-信息格式规范

对于提交时需要填写的 commit 信息，请遵守以下几点基本要求：

1.  commit 摘要请简要描述这一次 commit 改动的内容。注意 commit 摘要的长度不要超过 50 字符，超出的部分会自动置于正文中。
2.  如果需要进一步描述本次 commit 内容，请在正文中详细说明。

对于 commit 摘要，推荐按照如下格式书写：

```text
<修改类型>(<文件名>): <修改的内容>
```

修改类型分为如下几类：

-   `feat`：用于添加内容的情况。
-   `fix`：用于修正现有内容错误的情况。
-   `refactor`：用于对一个页面进行重构（较大规模的更改）的情况。
-   `revert`：用于回退之前更改的情况。

### pull-request-信息格式规范

对于 Pull Request，请遵守以下几点要求：

1.  标题请写明本次 PR 的目的（做了 **什么** 工作，修复了 **什么** 问题）。
2.  内容请简要叙述修改的内容。如果修复了一个 issue 的问题，请在内容中添加 `fix #xxxx` 字段，其中 `xxxx` 代表 issue 的编号。
3.  请您仔细阅读 [贡献指南](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) 和 [社区公约](https://github.com/OI-wiki/OI-wiki/blob/master/CODE_OF_CONDUCT.md)，并在同意后勾选 PR 模板中的框，表示您同意了以上指南和公约。

对于 Pull Request 的标题，推荐使用如下格式书写：

```plain
<修改类型>(<文件名>): <修改的内容> (<对应 issue 的编号>)
```

修改类型分为如下几类：

-   `feat`：用于添加内容的情况。
-   `fix`：用于修正现有内容错误的情况。
-   `refactor`：用于对一个页面进行重构（较大规模的更改）的情况。
-   `revert`：用于回退之前更改的情况。

示例：

-   `fix(ds/persistent-seg): 修改代码注释使描述更清晰`
-   `fix: tools/judger/index 不在目录中 (#3709)`
-   `feat(math/poly/fft): better proof`
-   `refactor(ds/stack): 整理页面内容`

### 协作流程

1.  在收到一个新的 Pull Request 之后，GitHub 会给 reviewer 发送邮件；
2.  与此同时，在 [GitHub Actions](https://github.com/frontecho/questmathdocs/actions) 上会运行测试，它会把进度同步在 PR 页面的下方。GitHub Actions 主要用来确认 PR 中内容的修改不会影响到网站构建的进程；Netlify 用来把 PR 中的更新构建出来，方便 reviewer 审核（在测试完成后点击 Details 可以了解更多）；
3.  reviewer 可能会发现问题，并提出 `review` 或 `suggested changes`（建议更改，显示为灰色图标）/`requested changes`（强制更改，显示为红色图标，只会在 reviewer 拥有 repo 写权限时出现）。一般来说，reviewer 也会附上建议和需要进行的更改，在这时，您将会需要继续向 Pull Request 追加其他更改。更改的方法可以参考 `在 GitHub 上编辑` 或者 `使用 Git 在本地进行编辑` 部分的 `向 Pull Request 追加更改` 部分。
4.  在足够多 reviewer 投票通过一个 PR 之后，这个 PR 才可以合并到 master 分支中；
5.  在合并到 master 分支之后，GitHub Actions 会重新构建一遍网站内容，并更新到 gh-pages 分支；
6.  这时服务器才会拉取 gh-pages 分支的更新，并重新部署最新版本的内容。

## markdown 基本语法与 mkdocs 特性
### 学习编写 markdown 文件
### Latex 公式
### mkdocs 特性

## 小插曲：VSCode的配置与插件
