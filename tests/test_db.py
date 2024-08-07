from fast_zero.models import User, table_registry
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select


def test_create_user(session):
    user = User(
        username='joao1',
        email='joao1@joao.com',
        password='qwerty_123',
        )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'joao1@joao.com')
            )
        
    assert result.username == 'joao1'