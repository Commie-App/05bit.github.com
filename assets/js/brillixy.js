hljs.initHighlightingOnLoad();

marked.setOptions({
    gfm: true,
    tables: true,
    breaks: false,
    pedantic: false,
    sanitize: false,
    smartLists: true,
    langPrefix: ''
});

$(function() {
    $('textarea.marked').each(function() {
        $(this).after(marked($(this).text())); 
    });
});
