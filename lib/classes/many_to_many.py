class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article not in self._articles:
            self._articles.append(article)
        return article
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list({article.magazine for article in self._articles})

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    def articles(self):
        return self._articles
    
    def contributors(self):
        return list({article.author for article in self._articles})
    
    def contributing_authors(self):
        author_counts = {}

        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._category = new_category

    

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
        author._articles.append(self)
        magazine._articles.append(self)
        
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")
