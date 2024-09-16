from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Categories(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.Integer, primary_key=True)  # Corrected 'db.column' to 'db.Column'
    name = db.Column(db.String(100), nullable=False)  # Corrected 'varchar' to 'String', and 'nullabe' to 'nullable'
class Menu_Items(db.Model):
    __tablename__ = 'Menu_Items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Changed 'decimal' to 'Numeric', and defined precision
    category_id = db.Column(db.Integer, db.ForeignKey('Categories.id'), nullable=False)  # Corrected id and column name
