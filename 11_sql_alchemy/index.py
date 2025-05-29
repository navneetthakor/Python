"""
sqlalchemy is one of the best orm in python to talk with relational databases
"""


from sqlalchemy import Integer, String, create_engine, ForeignKey,Column, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# establish connections
engine = create_engine("mysql+pymysql://sql12781914:DJ11B3jBph@sql12.freesqldatabase.com/sql12781914")

# define base mode
Base = declarative_base()

# define model
class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String(50)) # varchar(50)
    email = Column(String(50)) 

    # One-to-many relationship: one user can have many posts (for python side)
    # it is python side that's why 'Post' instead of 'posts' 
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50),unique=True,nullable=False)
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'),nullable=False)

    # Relationship back to user
    author = relationship("User", back_populates="posts")
    

# create table if it is not exists in db
Base.metadata.create_all(engine)

# create session 
Session = sessionmaker(bind=engine)
session = Session()

# drop all the existsting tables 
# Base.metadata.drop_all(bind=engine)
# result = session.execute(text('drop table if exists posts '))
# result = session.execute(text('drop table if exists users '))



# add user
# user1 = User(name="Navneet",email="codewithnavneet@gmail.com")
# session.add(user1)
# session.commit()

# post1 = Post(title="Hello brother",content="Nothing much",user_id=user1.id)
# session.add(post1)
# session.commit()

# adding one more book in second iteration --
user = session.query(User).filter(User.id==1).all()
post2 = Post(title="Hello brother 2",content="Nothing much",user_id=user[0].id)
session.add(post2)
session.commit()


# fetch all users
all_users = session.query(User).all()

for user in all_users:
    print(user.name, " , ", user.email, " , ", user.id)
    for post in user.posts:
        print(post.title)

# delete users 
# frist delete related post 
# result = session.query(Post).filter(Post.user_id == 2).delete()
# print(result)
# session.commit()

# now delete related data 
# result = session.query(User).filter(User.id == 2).delete()
# print(result)
# session.commit()
