from Post import TextPost, ImagePost, LinkPost, Post

class PostService:
    def create_post(self, post_type, **kwargs):
        """Create a new post."""
        try:
            post_classes = {'text': TextPost, 'image': ImagePost, 'link': LinkPost}
            if post_type not in post_classes:
                return "Invalid post type."
            post = post_classes[post_type](**kwargs)
            post.save()
            return f"{post_type.capitalize()} post created successfully."
        except Exception as e:
            return f"Error creating post: {e}"

    def get_post_by_id(self, post_id):
        """Retrieve a post by ID."""
        try:
            post = Post.objects(id=post_id).first()
            return post if post else "Post not found."
        except Exception as e:
            return f"Error fetching post: {e}"

    def update_post(self, post_id, update_data):
        """Update post details by ID."""
        try:
            post = Post.objects(id=post_id).first()
            if not post:
                return "Post not found."
            post.update(**update_data)
            return f"Post {post_id} updated successfully."
        except Exception as e:
            return f"Error updating post: {e}"

    def delete_post(self, post_id):
        """Delete a post by ID."""
        try:
            post = Post.objects(id=post_id).first()
            if not post:
                return "Post not found."
            post.delete()
            return f"Post {post_id} deleted successfully."
        except Exception as e:
            return f"Error deleting post: {e}"
