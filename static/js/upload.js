$(function () {
	$.ajax({
		type: "get",
		url: window.location.origin + "/about/json",
		dataType: "json",
		success: function (result) {
			showSideMenu(result);
		}
	});

	$("#navmenu").on("click", ".liname", function (index) {
		var index = $("#navmenu .liname").index(this);
		$("#navmenu>li>.child_menu").eq(index).slideToggle();
		$("#navmenu>li>.child_menu").eq(index).parent().siblings("li").find(".child_menu").slideUp();
	});
});

function showSideMenu(res) {
	// console.log(res.menuInfo)
	let menuInfo = res.menuInfo
	let childrenmenuInfo = res.childrenmunulist
	// console.log(res.childrenmunulist)

	for(var i = 0; i < menuInfo.length; i++) {
		var html = "";
		html += "<li>";
		html += "<a class='liname'><i class='fa fa-home'></i>" + menuInfo[i].menu_name + "<span class='fa fa-chevron-down'></span></a>";
		html += "<ul class='nav child_menu'>";
		for(var k = 0; k < childrenmenuInfo.length; k++) {
			if(childrenmenuInfo[k].menu_id == menuInfo[i].id) {
				html += "<li class='three_menu'>";
				html +=   "<a id= "+ childrenmenuInfo[k].children_code + " href='" + childrenmenuInfo[k].children_action + "'>" + childrenmenuInfo[k].children_name + "</a>";
				html += "<ul class='nav child_menu'>";
				html += "</ul>";
				html += "</li>";
			} 
		}
		html += "</ul>";
		html += "</li>";
		$("#navmenu").append(html);
	};




	$("#navmenu .child_menu").eq(0).css({
		"display": "block"
	});
	$("#navmenu .child_menu").eq(0).find("li:eq(0)").addClass("current-page");

	// var fram = "<iframe src=" + window.location + '/softupload'  + " name='myFrame' id='myIframe' width='100%' height='100%'  scrolling='auto' frameborder='0'></iframe>"
	// $("#rightContent").append(fram);

	$("#navmenu .child_menu").on("click", "li", function () {
		var index = $("#navmenu .child_menu li").index(this);
		$("#navmenu .child_menu li").eq(index).parent().parent().siblings("li").find(".child_menu").slideUp();
		$("#navmenu .child_menu li").eq(index).parent().parent().siblings("li").find(".child_menu").find("li").removeClass("current-page");
		$("#navmenu .child_menu li").eq(index).addClass("current-page")
		$("#navmenu .child_menu li").eq(index).siblings().removeClass("current-page");
	});


	$("#navmenu").on("click", ".three_menu", function () {
		var index = $("#navmenu .three_menu").index(this);
		$("#navmenu .three_menu .child_menu").eq(index).slideDown();
	});



	$("#navmenu .three_menu").on("click", "li", function () {
		var index = $("#navmenu .three_menu li").index(this);
		$("#navmenu .three_menu li a").eq(index).css({
			"color": "beige"
		});
		$("#navmenu .three_menu li a").eq(index).parent().siblings("li").find("a").css({
			"color": "white"
		});
	});

	function menuclick(){
		console.log('被点击了')
	}
	
	// const softUpload = document.getElementById("softUpload");
	// const pluginUpload = document.getElementById("pluginUpload");
	// const competition = document.getElementById("competition");
	
	// softUpload.addEventListener('click', menuclick, false);
	// pluginUpload.addEventListener('click', menuclick, false);
	// competition.addEventListener('click', menuclick, false);

	$(document).click(function (e) {
        var v_id = e.target.id;
        if (v_id=='softUpload'){
			console.log('跳转到' + v_id + '页面')
		}else if(v_id=='pluginUpload'){
			console.log('跳转到' + v_id + '页面')
		}
		else if(v_id=='competition'){
			console.log('跳转到' + v_id + '页面')
		}
    });
}




