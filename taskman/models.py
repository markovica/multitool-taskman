from core.database import db


class Workflow(db.Model):
    __tablename__ = 'workflows'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(50), nullable=False)
    description: str = db.Column(db.Text, nullable=False)
    graph_data: str = db.Column(db.json, nullable=False)

   

    def __repr__(self):
        return f'<Workflow {self.name!r}>'

'''
class PermissionRole(db.Model):
    __tablename__ = 'permission_role'
    permission_id = db.Column(db.Integer(), db.ForeignKey('permission.id', ondelete='CASCADE'), primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'), primary_key=True)


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # Relationships
    permissions = db.relationship('Permission', secondary=PermissionRole.__tablename__, back_populates='roles')


# Define the UserRoles association table
class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)

    # Relationships
    roles = db.relationship('Role', secondary=PermissionRole.__tablename__, back_populates='permissions')
'''