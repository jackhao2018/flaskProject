function musicPlay(ele) {
    let musicArea = document.createElement('div');
    let music = document.createElement('audio');
    let musicUl = document.createElement('ul');
    let a = 400;//歌词容器到高，随便改,但最好和你自己写到那个div一样高；
    let b = 35;//li的高度，无特殊要求；
    let c = 'demo.mp3'//歌曲目录，只能放一个哈！
    ele.appendChild(musicArea).appendChild(music);
    musicArea.appendChild(musicUl);
    musicStyle();
    let lrc = `[00:00.00] 作曲 : 薄荷映像
   [00:00.27] 作词 : 薄荷映像
   [00:00.81]早安喵 午安喵 晚安喵 喵 喵
   [00:05.82]早安喵 午安喵 晚安喵 喵 喵
   [00:20.94]喜欢你的微笑和调皮的嘴角
   [00:26.14]那午后的阳光穿过你的发梢
   [00:30.98]想让全世界停在这一秒
   [00:36.43]陪着你把世界都忘掉
   [00:41.49]早安喵 午安喵 晚安喵 喵 喵
   [00:46.30]早安喵 午安喵 晚安喵 喵 喵
   [01:11.25]喜欢你的微笑和调皮的嘴角
   [01:16.19]喜欢你的拥抱和黄色外套
   [01:21.06]这甜蜜的感觉只有我知道
   [01:27.14]就是喜欢你的味道
   [01:31.99]早安喵 午安喵 晚安喵 喵 喵
   [01:36.79]早安喵 午安喵 晚安喵 喵 喵
   [01:45.94]嘿咻嘿咻~
   `
    function musicStyle() {//控件css样式；	
        music.autoplay = true;
        music.src = c;
        music.controls = true;
        music.loop = true;
        music.style.outline = 'none';
        music.style.width = '100%';
        musicArea.style.width = '100%';
        musicArea.style.height = '100%';
        musicArea.style.overflow = 'hidden'
        // musicArea.style.outline ='3px solid'
        musicUl.style.listStyle = 'none';
        musicUl.style.width = '100%'
        musicUl.style.padding = '0';
        musicUl.style.transition = '0.3'
    }
    //把歌词变成[{time,lrc},{time,lrc}...]的样子，不然没法用的
    function split() {//把lrc歌词分割成数组，
        let split_1 = lrc.split('\n');
        let length = split_1.length;
        for (let i = 0; i < length; i++) {
            let lrcArr = split_1[i];
            split_1[i] = change(lrcArr);
            function change(str) {
                let lrc = str.split(']');
                let timer = lrc[0].replace('[', '');
                let str_music = lrc[1];
                let time_split = timer.split(':');
                let s = +time_split[1];
                let min = +time_split[0];
                return {
                    time: min * 60 + s,
                    lrc: str_music//分割好到歌词和时间
                }

            }
        }
        return split_1
    }
    let lrcArr = split();//至此歌词处理完了。
    createLi();
    function createLi() {//根据歌词数组创建li
        let len = lrcArr.length;
        for (let i = 0; i < len; i++) {
            let lrc_li = lrcArr[i];
            let li = document.createElement('li');
            li.innerText = lrc_li.lrc;
            li.style.height = b + 'px'
            li.style.textAlign = 'center'
            li.style.width = '100%'
            li.style.padding = '0';
            li.style.color = '#999'
            li.style.transition = '0.3'
            musicUl.appendChild(li);
        }
    }
    function setCurrentLi() {
        let time = music.currentTime;
        // console.log(time)
        for (i = 0; i < lrcArr.length; i++) {
            let play = lrcArr[i];
            if (time - play.time <= 0) {
                return i;
            }
        } return -1;
    }
    function current() {//设置top，让其滚动
        let li = setCurrentLi();
        let divHeight = a;
        let liHeight = b;
        let top = liHeight * li - divHeight / 2 + liHeight / 2;
        if (top < 0) {
            top = 0;
        }
        musicUl.style.marginTop = -top + 'px';
        // console.log('top'+top);
        let playLi = musicUl.querySelector('.play')
        if (playLi) {
            playLi.className = '';
        }
        if (li >= 0) {
            musicUl.children[li - 1].className = 'play'

        }
    }
    music.ontimeupdate = current;
}
