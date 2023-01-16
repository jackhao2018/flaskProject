// 立即执行函数
(function () {
  var Waterfall = function (opt) {
    this.el = document.getElementsByClassName(opt.el)[0]; // 实例
    this.oItems = this.el.getElementsByTagName('div') // 所有img的div集合类数组
    this.column = opt.column; // 列数
    this.gap = opt.gap // 间隙大小
    this.itemWidth = (this.el.offsetWidth - this.gap * (this.column - 1)) / this.column // 每张图片的大小: (父级容器大小 - 间隙大小) / 列数
    this.heightArr = [] // 每张图片高度数组
    // 启动函数
    this.init()
  }
  // 挂载到构造函数的原型上
  Waterfall.prototype.init = function () {
    this.render()
  }
  // 渲染函数
  Waterfall.prototype.render = function () {
    var item = null
    // 便利类数组的每一项
    for (let i = 0; i < this.oItems.length; i++) {
      // 每一项
      item = this.oItems[i]
      minIdx = -1
      item.style.width = this.itemWidth + 'px'
      // 计算第一排盒子的位置
      if (i < this.column) {
        item.style.top = '0px'
        // left: 当前图片的下标 * (每张图片大小+  实例大小)
        item.style.left = i * (this.itemWidth + this.gap) + 'px'
        this.heightArr.push(item.offsetHeight)
      } else {
        // 如果不是第一排 查找最小高度
        var minIdx = getMinIdx(this.heightArr)
        // 左边 类数组的最小左边距离
        item.style.left = this.oItems[minIdx].offsetLeft + 'px'
        // 高度 图片高度数组最小的值 + 间隙
        item.style.top = this.heightArr[minIdx] + this.gap + 'px'
        this.heightArr[minIdx] += item.offsetHeight + this.gap
      }
    }

    // 查找当前最小项函数
    function getMinIdx(arr) {
      return arr.indexOf(Math.min.apply(null, arr))
    }
  }

  // 全局用启动函数
  window.Waterfall = Waterfall
})()