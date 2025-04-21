from sqlalchemy.exc import IntegrityError

def safe_commit(session):
    try:
        session.commit()
        return {"success": True, "message": "Operação concluída com sucesso"}
    except IntegrityError as e:
        session.rollback()  # Evita transações corrompidas
        return {"success": False, "error": str(e.orig)}
