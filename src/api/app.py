"""
Модуль API для системи TMS.
"""
from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title='TMS API', version='1.0.0')


@app.get('/health')
def health_check():
    """
    Ендпоінт для перевірки працездатності сервісу.
    """
    return {
        'status': 'ok',
        'service': 'TMS',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    }