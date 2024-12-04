document.querySelectorAll('.upvote-thread').forEach(button => {
        console.log("Script added successfully")
        button.addEventListener('click', function() {
            const slug = button.getAttribute('data-slug');
            fetch(`/thread/${slug}/upvote/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.upvotes !== undefined) {
                    button.nextElementSibling.nextElementSibling.querySelector('.upvotes-count').textContent = data.upvotes;
                    button.nextElementSibling.nextElementSibling.querySelector('.downvotes-count').textContent = data.downvotes;
                }
            });
        });
    });

    document.querySelectorAll('.downvote-thread').forEach(button => {
        button.addEventListener('click', function() {
            const slug = button.getAttribute('data-slug');
            fetch(`/thread/${slug}/downvote/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.upvotes !== undefined) {
                    button.previousElementSibling.querySelector('.upvotes-count').textContent = data.upvotes;
                    button.previousElementSibling.querySelector('.downvotes-count').textContent = data.downvotes;
                }
            });
        });
    });

    // Do the same for comments
    document.querySelectorAll('.upvote-comment').forEach(button => {
        button.addEventListener('click', function() {
            const commentId = button.getAttribute('data-comment-id');
            fetch(`/comment/${commentId}/upvote/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.upvotes !== undefined) {
                    button.nextElementSibling.nextElementSibling.querySelector('.upvotes-count').textContent = data.upvotes;
                    button.nextElementSibling.nextElementSibling.querySelector('.downvotes-count').textContent = data.downvotes;
                }
            });
        });
    });

    document.querySelectorAll('.downvote-comment').forEach(button => {
        button.addEventListener('click', function() {
            const commentId = button.getAttribute('data-comment-id');
            fetch(`/comment/${commentId}/downvote/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.upvotes !== undefined) {
                    button.previousElementSibling.querySelector('.upvotes-count').textContent = data.upvotes;
                    button.previousElementSibling.querySelector('.downvotes-count').textContent = data.downvotes;
                }
            });
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
