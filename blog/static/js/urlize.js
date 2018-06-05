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
        var exp = /(\b(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;*]*[-A-Z0-9+&@#\/%=~_|])/ig;
        var attrs = blank ? "target='_blank' rel='noopener noreferrer' " : "";
        return text.replace(exp,"<a " + attrs + "href='$1'>$1</a>");
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
        console.log("!!!");
        var $text = $('#urlize-c'), $result = $('#urlize-r');
        console.log($text)
        var val = $text.val(), text = urlize($text.html());
        console.log(text);
        $result.html(text)[text ? 'show' : 'hide']();
    })

})(document, jQuery);
//var array = ['포도', '사과', '바나나', '망고'];
//
//for(var i in array) {
//    alert(array[i]);
//}