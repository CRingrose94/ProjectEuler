def reflect_inc(m_inc, x_inc, y_inc):

    # inc = incident, ref = reflected, tan = tangent

    m_tan = -4 * x_inc / y_inc
    m_ref = (2 * m_tan + m_inc * m_tan * m_tan - m_inc) / (1 + 2 * m_inc * m_tan - m_tan * m_tan)
    x_ref = -2 * m_ref * (y_inc - x_inc * m_ref) / (4 + m_ref * m_ref) - x_inc
    y_ref = m_ref * (x_ref - x_inc) + y_inc

    return m_ref, x_ref, y_ref


def compute(x, y):

    reflections = 0
    m = (-9.6 - 10.1) / (1.4 - 0.0)

    while abs(x) > 0.01 or y < 0:
        m, x, y = reflect_inc(m, x, y)
        reflections += 1

    return reflections


if __name__ == '__main__':

    print(compute(1.4, -9.6))
