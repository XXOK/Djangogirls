(function(d, $) {

    /** from moustache - https://github.com/janl/mustache.js/blob/master/mustache.js */
    var escapeMap = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': '&quot;',
        "'": '&#39;'
    };
    function escapeHTML(string) {
        return String(string).replace(/&(?!\w+;)|[<>"']/g, function (s) {
            return escapeMap[s] || s;
        });
    }
    /* **/

    /** from http://stackoverflow.com/questions/37684/how-to-replace-plain-urls-with-links
     *  (added blank option)
     */
    function replaceURLWithHTMLLinks(text, blank) {
//        var exp = /((https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig; //   보수적 방법
        var exp = /((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var foo = /([^http:/]+(www.)[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var foo2 = /([^ㄱ-힣]+(http:\/\/|https:\/\/)[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var foo3 = /([^a-zA-z]+(http:\/\/|https:\/\/)[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var foo4 = /(([+&@#\%?=~_|!,;*])[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var attrs = blank ? "target='_blank' rel='noopener noreferrer' " : "";
        console.log(text.match(foo4))
        if ( text.startsWith('www.') ) {
        return text.replace(exp,"<a " + attrs + "href='https://$1'>$1</a>");
        }
        else {
                if ( text.match(foo) ) {
                    return text.replace(exp,"<a " + attrs + "href='https://$1'>$1</a>");
                }
                if ( text.match(foo2) ) {
                    return text.replace(exp,"<a " + attrs + "href='$1'>$1</a>");
                }
                if ( text.match(foo3) ) {
                    return text.replace(exp,"<a " + attrs + "href='$1'>$1</a>");
                }
                if ( text.match(foo4) ) {
                    return text.replace(exp,"<a " + attrs + "href='https://$1'>$1</a>");
                }
                else {
                    return text.replace(exp,"<a " + attrs + "href='$1'>$1</a>");
                }
        }
    }

    /* **/

    function urlize(text) {
        var lines = text.split(/\r\n|\r|\n/g);
        for (var i=lines.length-1; i>=0; i--) {
            lines[i] = replaceURLWithHTMLLinks(escapeHTML(lines[i]), true);
        }
        return lines.join('<br>');
    }

//    var $text = $('#urlize-c'), $result = $('#urlize-r');
//    $result.hide();
//
//    $text.on('keyup change', function() {
//        var val = $text.val(),
//            text = urlize($text.val());
//        $result.html(text)[text ? 'show' : 'hide']();
//    }).trigger('change');
//
//    $result.show();

    $(document).ready(function() {
        var $text = $('#urlize-c'), $result = $('#urlize-r');
        var val = $text.val(), text = urlize($text.html());
        $result.html(text)[text ? 'show' : 'hide']();
    })

})(document, jQuery);
//var array = ['포도', '사과', '바나나', '망고'];
//
//for(var i in array) {
//    alert(array[i]);
//}