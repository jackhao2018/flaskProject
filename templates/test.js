function uploadvideo2(file) {
    let that=this
    let FileUrl = URL.createObjectURL(file) //文件转bold流
    let videoElenment = document.createElement('video');//创建一个视频控件
    videoElenment.src=FileUrl;//控件视频地址
    videoElenment.autoplay=true;//是否自动播放
    videoElenment.addEventListener("canplay",function(){//监听播放
      let canvas=document.createElement('canvas');//创建一个画板
      canvas.width=videoElenment.videoWidth * 0.8;//画板宽
      canvas.height=videoElenment.videoHeight * 0.8;//画板的高
      //通过画板的drawImage属性对图片进行处理
      canvas.getContext('2d').drawImage(videoElenment,0,0,canvas.width,canvas.height);
      //处理完毕通过toDataURL属性转为图片格式拿去base64图片路径
      let imgs=canvas.toDataURL('image/png')
      console.log(imgs)//视频第一帧图片路径
    })
};