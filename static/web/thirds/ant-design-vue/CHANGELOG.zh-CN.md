# 更新日志

`ant-design-vue` 严格遵循 [Semantic Versioning 2.0.0](http://semver.org/lang/zh-CN/) 语义化版本规范。

#### 发布周期

* 修订版本号：每周末会进行日常 bugfix 更新。（如果有紧急的 bugfix，则任何时候都可发布）
* 次版本号：带有新特性的向下兼容的版本。
* 主版本号：含有破坏性更新和新特性，不在发布周期内。

---

## 1.3.13
`2019-07-22`
- 🐞 修复 dist 缺少 antd.less 文件问题 [#995](https://github.com/vueComponent/ant-design-vue/issues/995)

## 1.3.12
`2019-07-22`
- 🐞 `package.json` `files` 添加 `scripts`

## 1.3.11
`2019-07-22`

- Dropdown
  - 🐞修复 `disable` 时的样式问题 [#912](https://github.com/vueComponent/ant-design-vue/pull/912) [#921](https://github.com/vueComponent/ant-design-vue/pull/921)
  - 🐞修复 `SubMenu` 闪动问题 [#975](https://github.com/vueComponent/ant-design-vue/issues/970)
- 🌟 `AutoComplete` `Cascader` `DatePicker` `DropDown` `Select` `TimePicker` 添加弹出内容的实例引用 `popupRef` [f9373e](https://github.com/vueComponent/ant-design-vue/commit/f9373e44ce229ab0ba94ababbd686e6ad6e9f10f)
- 🐞 修复 `DatePicker` 在ie 10 11下 placeholder 为中文时不能打开的问题 [#865](https://github.com/vueComponent/ant-design-vue/issues/865)
- 🌟 `DatePicker` 添加自定义渲染触发器功能  [#957](https://github.com/vueComponent/ant-design-vue/pull/957)
- 🌟 `@ant-design/icons-vue` 升级为 `^2.0.0`
- 🌟 `Icon` 添加属性 `focusable="false"` [#924](https://github.com/vueComponent/ant-design-vue/issues/924)
- 🐞 修复自定义 `Form` 校验自定义组件时提示 `warning` 问题 [#915](https://github.com/vueComponent/ant-design-vue/issues/915)
- 🐞 修复 `FormItem` `v-decorator` 指令报错问题 [#930](https://github.com/vueComponent/ant-design-vue/issues/930)
- 🐞 修复 `Upload` 组件在 `form.resetFields()` 时报错问题 [#929](https://github.com/vueComponent/ant-design-vue/pull/929)
- 🐞 修复 `Select` 显示跳动问题 [#970](https://github.com/vueComponent/ant-design-vue/issues/970)
- 🐞 修复 TypeScript 类型定义。

## 1.3.10
`2019-06-11`
- 🐞 移除打包后多余的 `module.export` [#850](https://github.com/vueComponent/ant-design-vue/issues/850)

## 1.3.9
`2019-05-26`
- 🐞 修复 `TreeSelect` 没有 `dataRef` 的问题 [#712](https://github.com/vueComponent/ant-design-vue/issues/712)
- 🌟 `Tooltip` 添加 `destroyTooltipOnHide` 用于标识隐藏后是否销毁tooltip [#727](https://github.com/vueComponent/ant-design-vue/issues/727)
- 🐞 修复 `Avatar` 动态设置 src 时不更新问题 [#731](https://github.com/vueComponent/ant-design-vue/issues/731)
- 🐞 修复 `LocaleProvider` 更改 `moment` 语言不生效问题 [28b7a6](https://github.com/vueComponent/ant-design-vue/commit/28b7a68dc48a0a994e98063d462b99380e3ee547)
- 🌟 `Modal.confirm` 新增 `closable` 配置 [#798](https://github.com/vueComponent/ant-design-vue/pull/798)
- 🐞 修复 `Select` 自定义 `dropdownRender` 时，没能自动关闭的问题 [#644](https://github.com/vueComponent/ant-design-vue/issues/644)
- 🐞 修复在 ie9 下移除 Dom 报错问题，无需单独引入 polyfill [#705](https://github.com/vueComponent/ant-design-vue/issues/705)
- 🐞 修复 `Input.Search` 重复挂载 id 问题 [#726](https://github.com/vueComponent/ant-design-vue/issues/726)
- 🐞 修复 `Table` 使用函数形式自定义 expandIcon 时不生效问题 [#751](https://github.com/vueComponent/ant-design-vue/issues/751)
- 🐞 修复 `Icon` extraCommonProps 属性不生效问题 [#737](https://github.com/vueComponent/ant-design-vue/issues/737)
- 🐞 修复 `DirectoryTree` expandAction="doubleclick" 不生效问题 [#745](https://github.com/vueComponent/ant-design-vue/issues/745)

## 1.3.8
`2019-04-04`
- 🐞 修复 `Table` 在 IE 下不可点击问题 [#504](https://github.com/vueComponent/ant-design-vue/issues/504)
- 🐞 修复 `Table` 在 Firefox 下 Header 没对齐问题 [#579](https://github.com/vueComponent/ant-design-vue/issues/579)
- 🌟 抽屉 `Drawer` 添加自定义 `handel` 功能
- 🐞 修复 TypeScript 类型定义。

## 1.3.7
`2019-03-18`
- 🐞 修复 `Select` `selectedKeys` 类型校验错误 [#597](https://github.com/vueComponent/ant-design-vue/issues/597)

## 1.3.6
`2019-03-17`
- 🐞 修复 `Select` title属性显示错乱问题 [#588](https://github.com/vueComponent/ant-design-vue/issues/588)
- 🐞 修复 `InputSearch` 不支持 slot 方式自定义 addonAfter 和 addonBefore 问题 [#581](https://github.com/vueComponent/ant-design-vue/issues/581)
- 🐞 修复 `Input` 重复 class 问题 [#faf9ba](https://github.com/vueComponent/ant-design-vue/commit/faf9ba0033eed9ae6ac17879f2e39dd341db847f)
- 🐞 修复 `Message` 通过函数自定义 content 不生效问题 [#554](https://github.com/vueComponent/ant-design-vue/issues/554)
- 🌟 `Cascader` 的 `option.value` 同时支持 `String` `Number` 类型 [#595](https://github.com/vueComponent/ant-design-vue/issues/595)
- 🐞 修复 TypeScript 类型定义。

## 1.3.5
`2019-02-23`

- 🌟 优化 `Popover` `Popconfirm` 组件箭头样式。
- 🐞 修复在 postcss（vue-cli）中使用 autoprefixer 9.4.5 会抛出错误 `Replace text-decoration-skip: ink to text-decoration-skip-ink: auto, because spec had been changed` 的问题。[#471](https://github.com/vueComponent/ant-design-vue/pull/471)
- Tree
  - 🐞 修复 Tree 节点内底部边距叠加的问题。[#502](https://github.com/vueComponent/ant-design-vue/issues/502)
  - 🐞 修复 `Tree` 结点无法拖拽插入目标结点问题。[#469](https://github.com/vueComponent/ant-design-vue/issues/502)
  - 📝 更新文档：`Tree` 组件 `dragxxx` 事件改成全小写。[#467](https://github.com/vueComponent/ant-design-vue/issues/467)
- 🐞 修复 `Modal.confirm` `class` 不生效问题。[#475](https://github.com/vueComponent/ant-design-vue/pull/475)
- 🐞 修复 TypeScript 类型定义。

## 1.3.4
`2019-01-31`

🎉 🎉 🎉 祝大家新年快乐！
- 🐞 修复AutoComplete组件disabled时，placeholder不显示的问题。[#402](https://github.com/vueComponent/ant-design-vue/issues/402)。
- 🐞 添加 `BreadcrmbItem` ts类型文件。[#452](https://github.com/vueComponent/ant-design-vue/issues/452)。
- 🐞 修复当FormItem在子组件中时不更新问题。[#446](https://github.com/vueComponent/ant-design-vue/issues/446)。
- 🐞 修复一些组件 TypeScript 定义。

## 1.3.3
`2019-01-26`

- 🐞 修复message在配置maxcount时，不能关闭提示窗问题。[#428](https://github.com/vueComponent/ant-design-vue/pull/428)。
- 🐞 修复一些组件 TypeScript 定义。[#422](https://github.com/vueComponent/ant-design-vue/pull/422)。
- 🌟 Anchor组件新增`warpperClass` `wrapperStyle`属性。[1aa42d](https://github.com/vueComponent/ant-design-vue/commit/1aa42dfe18bd7ac7893a765b6ee341844ea02550)
- 📝 更新文档：form增加preserve说明，icon修改自定义组件引用文档说明。

## 1.3.2
`2019-01-17`

- 🐞 修复Form在使用废弃API `autoCreateForm` 时报错问题。[#413](https://github.com/vueComponent/ant-design-vue/issues/413)。
- 🐞 修复Slider点击mark时报错问题。[#407](https://github.com/vueComponent/ant-design-vue/issues/407)。

## 1.3.1
`2019-01-15`

- 🐞 修复Table组件在ie下滚轮失效的问题。[#390](https://github.com/vueComponent/ant-design-vue/issues/390)。
- 🐞 修复Form没有清除不在需要校验字段问题。[#367](https://github.com/vueComponent/ant-design-vue/issues/367)。

## 1.3.0
`2019-01-12`

- 🎉 🎉 🎉 发布 vscode 插件 [ant-design-vue-helper](https://marketplace.visualstudio.com/items?itemName=ant-design-vue.vscode-ant-design-vue-helper)
- 🎉 🎉 🎉 优化官网文档交互

### 组件功能和样式同步到 antd 3.11.6 版本。
1.3.0 版本带来了两个新组件，还有很多激动人心的变化和新特性。

- 🔥 增加了一个新组件 [Comment](https://vue.ant.design/components/comment-cn/)。
- 🔥 增加了一个新组件 [ConfigProvider](https://vue.ant.design/components/config-provider-cn/) 为组件提供统一的全局化配置。

组件修复/功能增强：

- 🌟 Avatar 组件增加 `srcSet` 属性，用于设置图片类头像响应式资源地址。
- 🌟 Notification 组件增加 `onClick` 属性，点击通知时触发的回调函数。
- Transfer
  - 🌟 增加 `search` 事件，搜索框内容时改变时的回调函数，并废弃 `searchChange` 事件。
  - 🌟 增加 `disabled` 属性，用于禁用搜索框。
- 🌟 Badge 进行了重构，`count` 支持自定义组件。
- Slider
  - 🌟 增加 `tooltipVisible` 属性，用于 Tooltip 是否始终显示。
  - 🌟 优化focus效果
  - 🐞 修复键盘tab键聚焦时，Tooltip不显示问题。
  - 🐞 修复拖动时Tooltip不停的显隐切换问题。
- Calendar
  - 🌟 支持多种时间格式。
  - 🌟 showSearch 方法增加 `limit` 参数，用于限制搜索结果展示数量。
- Table
  - 🌟 增加 `expandIcon` 属性，用于自定义表格展开图标。
  - 🌟 customCell 方法增加 `index` 参数。
- Select
  - 🌟 增加 `removeIcon`、`clearIcon`、`menuItemSelectedIcon` 属性，用于自定义删除、清空、选中的图标。
  - 🌟 增加 `dropdownRender` 属性， 用于自定义下拉框内容。
  - 🌟 增加 `loading` 属性， 用于展示加载中状态。
- 🌟 优化 Button 在含有Icon时的显示效果。
- ⚡️ 重构 Tag 组件，简化代码并提升性能。
- 💄 Menu.Item 组件增加 `title` 属性，用于在收缩时展示的悬浮标题。
- 💄 微调 Card 头部和加载中的样式细节。
- 💄 优化 Spin 样式并略微提升了切换状态的性能。
- 🐞 修复 TextArea 组件高度不能自适应问题。
- 🐞 修复 Tooltip 在disabled状态下Button中，样式错误问题。[#389](https://github.com/vueComponent/ant-design-vue/issues/389)
- 🐞 修复一些组件 TypeScript 定义。


## 1.2.5
`2019-01-06`

- 🌟 新增`Typescript`类型文件[#250](https://github.com/vueComponent/ant-design-vue/issues/250)
- 🐞 修复`Icon`组件不能同时支持static class和dynamic class问题[#371](https://github.com/vueComponent/ant-design-vue/issues/371)

## 1.2.4
`2018-12-29`

- 🐞 修复`Select`组件没有触发`popupScroll`事件问题[#350](https://github.com/vueComponent/ant-design-vue/issues/350)
- 🐞 修复自定义`Icon`组件不支持`class` `style`问题。[#351](https://github.com/vueComponent/ant-design-vue/issues/351)
- 🌟 `Tree` `TreeSelect` 支持`number`类型的`key`。[#343](https://github.com/vueComponent/ant-design-vue/issues/343)
- 🌟 `Tree`组件`selectedKeys`、`expandedKeys`支持`.sync`修饰符。[6373ce](https://github.com/vueComponent/ant-design-vue/commit/6373ce8e92a979abb1f5dc94fa9697ee64b08dc2)
- `TreeSelect`
  - 🌟 `treeExpandedKeys`支持`.sync`修饰符。[983318](https://github.com/vueComponent/ant-design-vue/commit/983318b985ad727c008232c75a8598d52d0f924b)
  - 🐞 修复第一次`focus`时触发页面滚动问题。[139356](https://github.com/vueComponent/ant-design-vue/commit/1393563c9b7f8cb7d7ddc0409aa5422c53fca60b)
- 🐞 移除`Menu`组件初始化时的展开动画。[#338](https://github.com/vueComponent/ant-design-vue/issues/338)

## 1.2.3
`2018-12-25`

- 📝 移除圣诞彩蛋。
- 🐞 修复部分组件不支持数组类型`class`问题[#322](https://github.com/vueComponent/ant-design-vue/issues/322)
- 🌟 `TreeSelect` 组件新增 `treeExpandedKeys` 属性和 `treeExpand` 事件，用于控制树的展开收起。
- 🐞 修复`Tree`组件使用`TreeNode`时报重复`Key`问题。

## 1.2.2
`2018-12-19`

- 🐞 修复`Datepicker`渲染两次footer问题。[#315](https://github.com/vueComponent/ant-design-vue/issues/315)
- `Menu`
  - 🐞 修复在 `horizontal` 模式下不能自动收起来适应宽度的问题。[aa1b24](https://github.com/vueComponent/ant-design-vue/commit/aa1b2462cb333505d3efc53af1afb30fd0574dc7)。
  - 🐞 修复在 `inline` 模式下首次展开时没有动画的问题。[d63935](https://github.com/vueComponent/ant-design-vue/commit/d63935e50671fab2aa561a013c35af878c610c7c)
  - 🐞 修复`Menu`组件在`collapse=true` `openKeys=[]`时闪动问题。[3393f0](https://github.com/vueComponent/ant-design-vue/commit/3393f0e1513c5d29e2734397bb9e0c0b272c259f)
- 🐞 修复 `Form` 组件在设置`validateStatus`时缺少`Icon`问题。 [#321](https://github.com/vueComponent/ant-design-vue/issues/321)
- 🐞 修复 Upload 缩略图图标样式错误。[f1e130](https://github.com/vueComponent/ant-design-vue/commit/f1e130bdc0c12c625573c08a35c895b2d5d47568)
- 🐞 `Icon` 支持 native event [cffef3](https://github.com/vueComponent/ant-design-vue/commit/cffef392e5605de8d342787d7562e81ca8588800)


## 1.2.1
`2018-12-17`

- 🐞 修复`Menu`在`Layout`下伸缩时闪动问题
- 🐞 修复`Icon`报Warning问题

## 1.2.0
`2018-12-16`
### 与antd 3.10.x同步

- 🔥🔥🔥 使用了 svg 图标替换了原先的 font 图标，从而带来了以下优势：
  - 可以离线化使用，不需要从支付宝 cdn 下载字体文件，图标不会因为网络问题呈现方块，也无需字体文件本地部署。
  - 在低端设备上 svg 有更好的清晰度。
  - 支持多色图标。
  - 对于内建图标的更换可以提供更多 API，而不需要进行样式覆盖。
  - 😓 但同时带来打包文件过大问题，相关解决方案和讨论可以查看 React 版 ant-design [issue](https://github.com/ant-design/ant-design/issues/12011)。
  - 🌟 新增 `theme` 属性，可以设置图标的主题风格。
  - 🌟 新增 `component` 属性，可以外部传入一个组件来自定义控制渲染结果。
  - 🌟 新增 `twoToneColor` 属性，可以控制双色图标的主题色。
  - 🌟 新增静态方法 `Icon.getTowToneColor()` 和 `Icon.setTwoToneColor(...)`，可以全局性的获取和设置所有双色图标的主题色。
  - 🌟 新增静态方法 `Icon.createFromIconfontCN({...})`，可以更加方便地使用 [`iconfont.cn`](http://iconfont.cn/) 上托管的图标。
- 🔥 增加了一个新组件`Skeleton`
- 🔥 Menu 在 `horizontal` 模式下会自动收起来适应宽度。
- 🔥 Drawer 的 `placement` 支持 `top` 和 `bottom`，可以适应更多场景。
- 🌟 以下组件均新增了 `suffixIcon` 属性，用于设置输入框后面的图标，具体用法可以参考文档。
  - Cascader
  - DatePicker
  - Select
  - TreeSelect
  - TimePicker
- 🌟 新增 Modal.open 方法，用于可自定义图标的快捷对话框。
- 🌟 Modal.info 增加 `getContainer` 的配置。
- 🌟 合并优化了 RangePicker 的日历页脚 UI。
- 🌟 Anchor 组件增加 `click` 事件。
- 🌟 Tab 组件增加 `renderTabBar` 属性。
- 🌟 Input 组件增加 `select` 方法。
- 🌟 Steps 增加 `initial` 属性。
- 🌟 Upload 组件新增 `openFileDialogOnClick` 属性，用于设置点击组件时是否打开上传对话框。
- 🌟 InputNumber 组件新增 `decimalSeparator` 属性，用于设置自定义的小数点。
- 🐞 修复众多隐蔽暂未提issue的bug，再此不在一一列出

## 1.1.10

`2018-12-7`
- 🔥🔥🔥 在1.1.10版本中`Form`组件更好地支持单文件tempalte语法，在以往版本中，对于复杂的组件需求，需要使用JSX才可以实现。为了更好地在template中使用Form表单的自动收集校验功能，我们优化了组件的使用方式。文档全部Demo使用最新语法重构。
不过对于以往API，还是继续支持，你可以不用担心API的改变，导致已有系统出现问题。
````html
<template>
  <a-form :form="form">
    <a-form-item>
      <a-input v-decorator="[id, options]">
    </a-form-item>
  </a-form>
</template>
<script>
export default {
  beforeCreate () {
    this.form = this.$form.createForm(this, options)
  },
}
</script>
````
- 🐞 修复`Steps`组件`labelPlacement`不生效问题 [#281](https://github.com/vueComponent/ant-design-vue/issues/281)
- 🐞 修复`Timeline`组件样式问题，添加`reverse` `mode`属性 [#8e37cd](https://github.com/vueComponent/ant-design-vue/commit/8e37cd89f92ee2541f641fd860785cfd2361b2b3)
- `Tree`
  - 🐞 修复`treeDefaultExpandedKeys`不生效问题 [#284](https://github.com/vueComponent/ant-design-vue/issues/284)
  - 🐞 修复`expandedKeys` `selectedKeys`等其它数组属性通过组件变异方法改变时组件不更新问题 [#239](https://github.com/vueComponent/ant-design-vue/issues/239)


---

## 1.1.9

`2018-11-26`
- 🐞 修复`TreeSelect`组件getPopupContainer不生效问题 [#265](https://github.com/vueComponent/ant-design-vue/issues/265)
- 🐞 修复`Carousel`组件按需加载不生效问题 [#271](https://github.com/vueComponent/ant-design-vue/issues/271)
- 🐞 修复`Upload`组件remove事件无返回值问题 [#259](https://github.com/vueComponent/ant-design-vue/issues/259)


## 1.1.8

`2018-11-11`
- `Progress`
  - 🐞 修复circle类型不支持strokeColor问题 [#238](https://github.com/vueComponent/ant-design-vue/issues/238)
  - 🐞 添加`normal`类型 [#257](https://github.com/vueComponent/ant-design-vue/issues/257)
- 🐞 修复`Cascader`组件getPopupContainer不生效问题 [#257](https://github.com/vueComponent/ant-design-vue/issues/257)
- 🌟 `Tooltip`支持align [#252](https://github.com/vueComponent/ant-design-vue/issues/252)


## 1.1.7

`2018-10-27`
- 🐞 修复`Cascader`组件类型错误问题 [#219](https://github.com/vueComponent/ant-design-vue/issues/219)
- 🐞 修复`Tree`组件自定义Icon时回调参数顺序错误问题 [#223](https://github.com/vueComponent/ant-design-vue/issues/223)
- 🐞 修复`Table`组件多次触发翻页回调问题 [#228](https://github.com/vueComponent/ant-design-vue/issues/228)
- 🌟 优化`Tabs`组件新增tab默认滚动到可视区域 [#215](https://github.com/vueComponent/ant-design-vue/issues/215)
- 🐞 修复`RadioGroup`组件不支持数字0问题 [#226](https://github.com/vueComponent/ant-design-vue/issues/226)
- 🐞 修复`Slider`组件当设置zoom不为1时，位置错误问题，部分浏览器需要visualViewport Polyfill [#227](https://github.com/vueComponent/ant-design-vue/issues/227)

## 1.1.6

`2018-10-10`
- 🐞 修复`Select`组件键盘事件报错问题 [#217](https://github.com/vueComponent/ant-design-vue/issues/217)
- 🐞 修复`Drawer`组件children更新问题 [#209](https://github.com/vueComponent/ant-design-vue/issues/209)

## 1.1.4

`2018-09-29`
- 🛠 重构`vc-tree`组件，并新增目录树组件
- 🐞 修复`tabs`组件属性`tabBarGutter`不生效问题 [#205](https://github.com/vueComponent/ant-design-vue/issues/205)
- 🐞 修复`table`组件数据同步出错问题 [#202](https://github.com/vueComponent/ant-design-vue/issues/202)

## 1.1.3

`2018-09-22`
- 🎉 优化组件注册方式，如Vue.use(Form) [a6620c](https://github.com/vueComponent/ant-design-vue/commit/a6620cbbe58cc1694a994e6714853906d1d794be)
- 🐞 `Select.Option` 组件`value`属性支持`0` [#194](https://github.com/vueComponent/ant-design-vue/issues/194)
- 🐞 修复 `Layout.Sider` 折叠按钮宽度不生效问题 [#201](https://github.com/vueComponent/ant-design-vue/issues/201)
- 🐞 修复 `Menu` 切换inlineCollapsed时，纵向无动画问题 [#200](https://github.com/vueComponent/ant-design-vue/issues/200)
- 🐞 修复 `Steps` `dot`模式下样式问题 [#199](https://github.com/vueComponent/ant-design-vue/issues/199)


## 1.1.2

`2018-09-17`
- 🎉 同步antd3.8.4样式
- 🌟 Tag组件新增`visible`属性及wave效果
- 🐞 修复`Cascader`组件，已选中项未展开问题 [#195](https://github.com/vueComponent/ant-design-vue/issues/195)

## 1.1.1

`2018-09-13`
- 🐞 修复窗口大小改变导致弹窗位置错位问题 [#184](https://github.com/vueComponent/ant-design-vue/issues/184)
- 🐞 tabs容器添加自定义事件监听 [#189](https://github.com/vueComponent/ant-design-vue/issues/189)
- 🐞 修复通过API形式调用Modal窗口时，`centered`不生效问题 [#183](https://github.com/vueComponent/ant-design-vue/issues/183)
- 🐞 Slider marks支持{number: function}形式 [#171](https://github.com/vueComponent/ant-design-vue/issues/171)

## 1.1.0

`2018-09-11`
- 🎉 从[3.4.0](https://github.com/ant-design/ant-design/releases/tag/3.4.0)同步组件到antd [3.8.2](https://github.com/ant-design/ant-design/releases/tag/3.8.2)
- 🌟 新增`Drawer 抽屉`组件
- 🐞 修复`Spin`内容闪烁问题 [#174](https://github.com/vueComponent/ant-design-vue/issues/174)
- 🐞 修复`RangePicker`选择项未禁用问题 [#158](https://github.com/vueComponent/ant-design-vue/issues/158)
- 🐞 修复`Form`值为 `null`时报错问题 [#153](https://github.com/vueComponent/ant-design-vue/issues/153)
- 🐞 修复`Modal`子组件重复`mounted`问题 [#152](https://github.com/vueComponent/ant-design-vue/issues/152)
- 🐞 修复`Transfer`搜索过滤后不能正确显示问题 [#148](https://github.com/vueComponent/ant-design-vue/issues/148)
- 🐞 修复多级`Tabs`组件嵌套导致`size`不生效问题 [#144](https://github.com/vueComponent/ant-design-vue/issues/144)
- 🐞 修复`TreeSelect`searchPlaceholder 不生效 [#125](https://github.com/vueComponent/ant-design-vue/issues/125)
- 🛠 其它未出现在issue中的问题，详见antd changelog

## 1.0.3

`2018-08-11`
- 🐞 修复`Select`子元素不更新问题 [#106](https://github.com/vueComponent/ant-design-vue/issues/106)
- 🐞 修复`Badge` offset属性X Y轴顺序错误问题，并新增支持number类型 [#99](https://github.com/vueComponent/ant-design-vue/issues/99)
- 🐞 修复`Input`在ie下中文placeholder触发input事件问题 [#92](https://github.com/vueComponent/ant-design-vue/issues/92)
- 🐞 修复`Avatar`不接受事件问题 [#102](https://github.com/vueComponent/ant-design-vue/issues/102)
- 🐞 修复`grid.row`gutter类型错误问题 [4af03c4](https://github.com/vueComponent/ant-design-vue/commit/4af03c4ab9596ede9d1b79c8308d0a3ed58b7a11)
- 🐞 修复`CheckboxGroup`在`Form`中报defaultValue warning问题 [#110](https://github.com/vueComponent/ant-design-vue/issues/110)

## 1.0.2

`2018-08-04`
- 🎉 修改组件库名称为`ant-design-vue`
- 🌟 官方站点支持IE9访问[a8a5f8](https://github.com/vueComponent/ant-design-vue/commit/a8a5f854c3b6a78df526caf2fb391e5c9d0848ac)
- 🐞 修复导出未定义变量引起的提醒问题[#87](https://github.com/vueComponent/ant-design-vue/issues/87)
- 🐞 修复部分组件类名重复问题[b48bbac](https://github.com/vueComponent/ant-design-vue/commit/b48bbac695dabec9160d947f9b27b2d91028c455)
- 🐞 修复`Select`组件label不更新问题[da1b924](https://github.com/vueComponent/ant-design-vue/commit/da1b924cba0fcc871b73590ac3ebd96af81b3897)
- 🛠 更正了若干文档错误

## 1.0.1

`2018-07-27`
- 🌟 针对`Input`组件优化中文输入(仅在v-model绑定时生效) [4a5154](https://github.com/vueComponent/ant-design-vue/commit/4a51544bd6470ab628dda80e9d7593e4603dd0b6)
- 🐞 修复`TreeSelect` `treeeData[i].children`为`null`时报错问题[#81](https://github.com/vueComponent/ant-design-vue/issues/81)
- 🐞 修复`Calendar`组件的 change 事件触发两次的问题[#82](https://github.com/vueComponent/ant-design-vue/issues/82)
- 🐞 修复`Card`组件的`description`和`title`属性slot不生效问题[#83](https://github.com/vueComponent/ant-design-vue/issues/83)
- 🐞 修复`DataPicker`组件的`dropdownClassName`属性不生效问题[02ab242](https://github.com/vueComponent/ant-design-vue/commit/02ab242197b923f2157f41d98a7930512475a799)

## 1.0.0

`2018-07-21`
- 🌟 新增`Carousel 走马灯`组件[edddbd](https://github.com/vueComponent/ant-design-vue/commit/edddbd982a279b62229ce825855c14c556866ece)
- 更正了若干文档错误

## 0.7.1

`2018-07-17`
- 🐞 修复`Tooltip`包含`Button`时的样式及功能问题[#73](https://github.com/vueComponent/ant-design-vue/issues/73)
- 🐞 add `Table` panagation deep watch[#b464c6](https://github.com/vueComponent/ant-design-vue/commit/b464c6f6ee4df6df1b6c55f29ac85b2f462763bc)


## 0.7.0

`2018-07-11`
- 🌟 新增`TreeSelect`组件
- 🌟 `Select`组件新增`options`，方便直接生成选择列表[#37](https://github.com/vueComponent/ant-design-vue/issues/37)
- 🐞 修复`Tooltip`中使用`Select`组件时，`blur`事件报错问题[#67](https://github.com/vueComponent/ant-design-vue/issues/67)
- 🐞 修改`Upload`组件`action`属性为可选[#66](https://github.com/vueComponent/ant-design-vue/issues/66)


## 0.6.8

`2018-07-05`
- 🐞 修复`notification` h is not defined[#63](https://github.com/vueComponent/ant-design-vue/issues/63)
- 🐞 修复`Transfer`国际化缺少titles问题[#64](https://github.com/vueComponent/ant-design-vue/issues/64)


## 0.6.7

`2018-07-03`
- 🐞 修复`Form`使用模板语法时组件不能更新[#62](https://github.com/vueComponent/ant-design-vue/issues/62)

## 0.6.6

`2018-07-03`
- 🐞 修复`Upload`的类型校验错误问题并更新相关demo[#61](https://github.com/vueComponent/ant-design-vue/issues/61)
- 🐞 修复`Upload`图片预览不能正确跳转问题[1584b3](https://github.com/vueComponent/ant-design-vue/commit/1584b3839e500d2d6b07abf704f5cd084ca00e87)


## 0.6.5

`2018-07-01`
- 🐞 修复`Select`的`getPopupContainer`不生效问题[#56](https://github.com/vueComponent/ant-design-vue/issues/56)
- 🐞 修复`Select`的弹出框位置不更新问题[8254f7](https://github.com/vueComponent/ant-design-vue/commit/8254f783a32189b63ffcf2c53702b50afef1f3db)

## 0.6.4

`2018-06-28`
- 🐞 修复`InputSearch`的`v-model`返回值错误问题[#53](https://github.com/vueComponent/ant-design-vue/issues/53)

## 0.6.3

`2018-06-26`
- 🐞 修复`Popover`的`v-model`不生效问题[#49](https://github.com/vueComponent/ant-design-vue/issues/49)

## 0.6.2

`2018-06-24`
- 🌟 `Form`组件数据自动校验功能支持`template`语法[7c9232](https://github.com/vueComponent/ant-design-vue/commit/7c923278b3678a822ff90da0cb8db7653d79e15c)
- `Select`: 🐞 添加`focus` `blur`方法[52f6f5](https://github.com/vueComponent/ant-design-vue/commit/52f6f50dbe38631c0e698a6ea23b3686f6c2a375)
- `Radio`
  - 🐞 修复Radiogroup `disabled` className[9df74b](https://github.com/vueComponent/ant-design-vue/commit/9df74bedd7640b6066010c498f942ce544c658b7)
  - 🐞 修复`autoFoucs` `focus` `blur` `mouseenter` `mouseleave` 不生效问题[f7886c](https://github.com/vueComponent/ant-design-vue/commit/f7886c7203730bedf519bc45f5f78726735d3aac)
- `TimePicker`: 🐞 修复`autoFoucs` `focus` `blur`不生效问题[28d009](https://github.com/vueComponent/ant-design-vue/commit/28d009d3ced807051a86a2c09cd2764303de98f7)


## 0.6.1

`2018-06-17`
- 🌟 新增`List`列表组件
- `Table`
  - 🐞 修复更新高度时报错问题[#33](https://github.com/vueComponent/ant-design-vue/issues/33)
  - 🐞 修复`defaultChecked`不生效问题[ec1999](https://github.com/vueComponent/ant-design-vue/commit/ec1999dea4cea126b78e3fd84bef620b876e9841)
  - `columns key`支持数字类型[9b7f5c](https://github.com/vueComponent/ant-design-vue/commit/9b7f5c2f81b6f83190e5b022b2b1e28de3f68a2b)
- `Tooltip`
  - 🛠 更新事件API`change`为`visibleChange`
- `Textarea`: 🐞 修复`autoFoucs`不生效问题[787927](https://github.com/vueComponent/ant-design-vue/commit/787927912307db7edb9821a440feacd216e3a6a2)
- `InputSearch`: 🐞 添加`focus` `blur`方法[3cff62](https://github.com/vueComponent/ant-design-vue/commit/3cff62997d16811ae17618f9b41617973d805d7d)
- `InputNumber`: 🐞 修复`autoFoucs`不生效问题[88f165](https://github.com/vueComponent/ant-design-vue/commit/88f165edb5c3993f4dba90c3267a1ea037e0869b)
- `DatePicker`: 🐞 修复`autoFoucs`不生效问题[264abf](https://github.com/vueComponent/ant-design-vue/commit/264abff59791181b9190ca0914b780a8df6aa81a)
- `Cascader`: 🐞 修复`autoFoucs`不生效问题[be69bd](https://github.com/vueComponent/ant-design-vue/commit/be69bd9af1bae184a4ebe8c4ef9560479ab11027)
- `Rate`: 🐞 修复`autoFoucs`不生效问题，及`blur`报错问题[c2c984](https://github.com/vueComponent/ant-design-vue/commit/c2c9841eb9b8e5ce4decff57a925e60d4bd7d809)
- `RangePicker`: 🐞 修复值类型校验出错问题[228f44](https://github.com/vueComponent/ant-design-vue/commit/228f4478a5d169d22960c97d1d8a8320c58da9cc)


## 0.6.0

`2018-06-04`
- 🌟 新增`Anchor`锚点组件
- `Table`
  - 🐞 修复`loading.spinning`时显示`emptyText`问题[17b9dc](https://github.com/vueComponent/ant-design-vue/commit/17b9dc14f5225eb75542facdb5053f4916b9d77f)
  - 🐞 修复`header style`不生效问题[#30](https://github.com/vueComponent/ant-design-vue/pull/30)
- `DatePicker`: 🐞 修复属性`showTime`为`true`时，重复调用`change`事件问题[81ab82](https://github.com/vueComponent/ant-design-vue/commit/81ab829b1d0f67ee926b106de788fc5b41ec4f9c)
- `InputNumber`: 🐞 修复`placeholder`不生效问题[ce39dc](https://github.com/vueComponent/ant-design-vue/commit/ce39dc3506474a4b31632e03c38b518cf4060cef#diff-c9d10303f22c684e66d71ab1f9dac5f9R50)


## 0.5.4

`2018-05-26`
- 🐞 修复dist目录缺少less文件问题[ca084b9](https://github.com/vueComponent/ant-design-vue/commit/ca084b9e6f0958c25a8278454c864ac8127cce95)

## 0.5.3

`2018-05-25`
- 🐞 修复构建`antd-with-locales.js`包含测试文件的问题[90583a3](https://github.com/vueComponent/ant-design-vue/commit/90583a3c42e8b520747d6f6ac10cfd718d447030)

## 0.5.2

`2018-05-25`

- 🐞 `Timeline`: 修复重复显示loading组件bug[fa5141b](https://github.com/vueComponent/ant-design-vue/commit/fa5141bd0061385f251b9026a07066677426b319)
- `Transfer`
  - 🐞 修复搜索框的清除按钮不起作用问题[4582da3](https://github.com/vueComponent/ant-design-vue/commit/4582da3725e65c47a542f164532ab75a5618c265)
  - 💄 重写了属性变化监听逻辑，避免不必要的[0920d23](https://github.com/vueComponent/ant-design-vue/commit/0920d23f12f6c133f667cd65316f1f0e6af27a33)
- 💄 `Select`: 优化`title`显示逻辑[9314957](https://github.com/vueComponent/ant-design-vue/commit/931495768f8b573d12ce4e058e853c875f22bcd3)
- `Form`
  - 🐞 修复Form组件指令报错问题[#20](https://github.com/vueComponent/ant-design-vue/issues/20)
  - 🌟 优化获取Form包装组件实例功能[c5e421c](https://github.com/vueComponent/ant-design-vue/commit/c5e421cdb2768e93288ce7b4654bee2114f8e5ba)
- 🐞 `DatePicker`: 修复日历键盘事件不起作用问题[e9b6914](https://github.com/vueComponent/ant-design-vue/commit/e9b6914282b1ac8d84b4262b8a6b33aa4e515831)
- `Avatar`: 修复字体大小自适应问题[#22](https://github.com/vueComponent/ant-design-vue/pull/22)
- 🌟 添加了部分组件的单测
- 🌟 整理了组件库依赖(dependencies、devDependencies)，删除不再使用的包，并添加peerDependencies


## 0.5.1

`2018-05-10`

- 🐞 `Table`: 修复 `customRow` 自定义事件不生效问题[#16](https://github.com/vueComponent/ant-design-vue/issues/16)

## 0.5.0

`2018-05-08`

- 🌟 `Form `新增Form表单组件
- 💄 `Upload.Dragger`: 修改组件name名称为`a-upload-dragger`
- 🐞 `Upload`: 修复Upload name属性失效问题


## 0.4.3

`2018-05-02`

- 🐞 修复组件样式丢失问题
- 🌟 站点添加babel-polyfill

## 0.4.2

`2018-04-24`

- 🐞  修复menu 非 inline 模式下的 click bug

## 0.4.1

#### bug

- 将Vue依赖转移到devDependencies，避免与业务版本不一致导致的不稳定bug

## 0.4.0

#### Layout

- 新增 Layout 组件

#### 其它

- 支持导入所有组件[Vue.use(antd)](https://github.com/vueComponent/ant-design-vue/issues/3)


## 0.3.1

#### Features

- 对外第一个版本，提供常用45个[组件](https://github.com/vueComponent/ant-design-vue/blob/c7e83d6142f0c5e72ef8fe794620478e69a50a8e/site/components.js)

