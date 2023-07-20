from sqlalchemy import create_engine, text
import os

WELLS_URL = 'postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells'
# eh, I'll figure out how to do the environmental variable later
def query_db(min_depth, min_gradient):
    """Returns wells that fit the search criteria."""

    engine = create_engine(WELLS_URL)
    
    query = text(
            """SELECT latitude, longitude, depth, gradient
            FROM wells
            WHERE depth > :min_depth AND gradient > :min_gradient
            """
            )
    with engine.connect() as conn:
        results = (
                conn
                .execute(query, {'min_depth': min_depth, 'min_gradient': min_gradient})
                .fetchall()
                )

    return results

if __name__ == '__main__':
    print(WELLS_URL)
    import sys

    min_depth = float(sys.argv[1])
    min_gradient = float(sys.argv[2])

    print(query_db(min_depth, min_gradient))

