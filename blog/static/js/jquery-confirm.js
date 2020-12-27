$(document).on('click', '.delete-post, .comment-approve, .publish-post', function(){
    return confirm(`Are you sure you want to do this?`);
})
