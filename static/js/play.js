function musicPlay(ele){
    let musicArea = document.createElement('div');
    let music =document.createElement('audio');
    let musicUl =document.createElement('ul');
    let a = 400;//歌词容器到高，随便改,但最好和你自己写到那个div一样高；
    let b = 35;//li的高度，无特殊要求；
    let c ='../static/audio/You Know What.mp3'//歌曲目录，只能放一个哈！
    ele.appendChild(musicArea).appendChild(music); musicArea.appendChild(musicUl);
    musicStyle();

    let lrc = `[ti:对面的女孩看过来]
    [ar:任贤齐]
    [by:http://www.lrcgeci.com]
    [00:05.90]（咳!）对面的女孩看过来
    [00:09.99]看过来，看过来
    [00:13.81]这里的表演很精彩
    [00:17.46]请不要假装不理不睬
    [00:21.99]
    [00:23.34]对面的女孩看过来
    [00:26.85]看过来，看过来
    [00:30.49]不要被我的样子吓坏
    [00:34.11]其实我很可爱
    [00:39.50]寂寞男孩的悲哀
    [00:43.18]说出来，谁明白
    [00:46.99]求求你抛个媚眼过来
    [00:50.56]哄哄我
    [00:52.05]逗我乐开怀
    [00:56.84]（嘿嘿嘿，没人理我，嘿！）
    [00:59.71]我左看右看，上看下看
    [01:03.70]原来每个女孩都不简单
    [01:06.98]我想了又想，我猜了又猜
    [01:10.74]女孩们的心事还真奇怪
    [01:15.50]
    [01:31.43]寂寞男孩的苍蝇拍
    [01:35.09]左拍拍，右拍拍
    [01:38.80]为什么还是没人来爱
    [01:42.30]无人问津哪，真无奈
    [01:45.95]
    [01:48.21]对面的女孩看过来
    [01:51.38]看过来，看过来
    [01:55.14]寂寞男孩情豆初开
    [01:58.64]需要你给我一点爱
    [02:03.66]（嗨----嗨----！）
    [02:08.01]我左看右看，上看下看
    [02:11.79]原来每个女孩都不简单
    [02:15.25]我想了又想，我猜了又猜
    [02:19.10]女孩们的心事还真奇怪
    [02:22.68]我左看右看，上看下看
    [02:26.51]原来每个女孩都不简单
    [02:29.85]我想了又想，我猜了又猜
    [02:33.74]女孩们的心事还真奇怪
    [02:37.87]爱真奇怪！
    [02:40.10]唻唻唻......喔哎噢！
    [02:46.48]唻唻唻......噢----！
    [02:53.91]
    [02:57.94]（唉！算了，回家吧！）`

    // function musicStyle(){//控件css样式；	
    //     music.autoplay =true;
    //     music.src =c;	
    //     music.controls =true;
    //     music.loop =true;
    //     music.style.outline ='none'; 
    //     music.style.width ='100%';
    //     musicArea.style.width ='100%';
    //     musicArea.style.height ='100%';
    //     musicArea.style.overflow = 'hidden'
    //     // musicArea.style.outline ='3px solid'
    //     musicUl.style.listStyle ='none'; 
    //     musicUl.style.width ='100%'
    //     musicUl.style.padding  ='0';
    //     musicUl.style.transition = '0.3'
    // }
    //把歌词变成[{time,lrc},{time,lrc}...]的样子，不然没法用的
    function split(){//把lrc歌词分割成数组，
       let split_1 =lrc.split('\n');
       let length = split_1.length;
       for (let i = 0; i < length; i++) {
           let lrcArr = split_1[i];
           split_1[i] = change(lrcArr);
       function change(str){
           let lrc = str.split(']');
           let timer =lrc[0].replace('[','');
           let str_music =lrc[1];
           let time_split =timer.split(':');
           let s = +time_split[1];
           let min = +time_split[0];
           return{
               time:min*60 + s ,
               lrc :str_music//分割好到歌词和时间
           }
           
       }
   }
   return split_1
   }
   let lrcArr = split();//至此歌词处理完了。
   createLi();
   function createLi(){//根据歌词数组创建li
       let len = lrcArr.length;
       for (let i = 0; i < len; i++) {
             let lrc_li  = lrcArr[i];
             let li  = document.createElement('li');
             li.innerText =lrc_li.lrc;
             li.style.height = b + 'px'
             li.style.textAlign ='center'
             li.style.width='100%'
             li.style.padding = '0';
             li.style.color = '#999'
             li.style.transition = '0.3'
             musicUl.appendChild(li);
       }
   }
   function setCurrentLi(){
       let time = music.currentTime;
       for ( i = 0; i < lrcArr.length; i++) {
           let play = lrcArr[i];
           if (time -play.time <= 0) {
                return i;
           }
       }return -1;
   }
   function current(){//设置top，让其滚动
       let li = setCurrentLi();
       let divHeight = a;
       let liHeight =b;
       let top  = liHeight*li - divHeight / 2 +liHeight / 2;
       if (top < 0) {
           top = 0;
       }
       musicUl.style.marginTop = -top + 'px';
       // console.log('top'+top);
       let playLi =musicUl.querySelector('.play')
       if (playLi) {
           playLi.className = '';		
       }
       if(li>=0){
           musicUl.children[li-1].className ='play'
       
   }}
   music.ontimeupdate = current;
   }
   