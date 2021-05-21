(function ($) {
    "use strict"; // Start of use strict

    // Toggle the side navigation
    $("#sidebarToggle, #sidebarToggleTop").on('click', function (e) {
        $("body").toggleClass("sidebar-toggled");
        $(".sidebar").toggleClass("toggled");
        if ($(".sidebar").hasClass("toggled")) {
            $('.sidebar .collapse').collapse('hide');
        }
        ;
    });

    // Close any open menu accordions when window is resized below 768px
    $(window).resize(function () {
        if ($(window).width() < 768) {
            $('.sidebar .collapse').collapse('hide');
        }
        ;
    });

    // Prevent the message wrapper from scrolling when the fixed side navigation hovered over
    $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function (e) {
        if ($(window).width() > 768) {
            var e0 = e.originalEvent,
                delta = e0.wheelDelta || -e0.detail;
            this.scrollTop += (delta < 0 ? 1 : -1) * 30;
            e.preventDefault();
        }
    });


    /* js代码 */
    var topBtn = document.getElementById('top');
    // 获取视窗高度
    var winHeight = document.documentElement.clientHeight;
    window.onscroll = function () {
        // 获取页面向上滚动距离，chrome浏览器识别document.body.scrollTop，而火狐识别document.documentElement.scrollTop，这里做了兼容处理
        var toTop = document.documentElement.scrollTop || document.body.scrollTop;
        // 如果滚动超过一屏，返回顶部按钮出现，反之隐藏
        if (toTop >= winHeight) {
            topBtn.style.display = 'block';
        } else {
            topBtn.style.display = 'none';
        }
    }
    topBtn.onclick = function () {
        var timer = setInterval(function () {
            var toTop = document.documentElement.scrollTop || document.body.scrollTop;
            // 判断是否到达顶部，到达顶部停止滚动，没到达顶部继续滚动
            if (toTop == 0) {
                clearInterval(timer);
            } else {
                // 设置滚动速度
                var speed = Math.ceil(toTop / 5);
                // 页面向上滚动
                document.documentElement.scrollTop = document.body.scrollTop = toTop - speed;
            }
        }, 50);
    }
})(jQuery); // End of use strict
