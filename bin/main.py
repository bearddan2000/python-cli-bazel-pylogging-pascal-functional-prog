import logging

logging.basicConfig(level=logging.INFO)

"""Find the binomial coefficent."""
def row(k, i, c):
    if k > i:
        return;
    logging.info( "%d, " % c);
    a = c * (i-k)/(k+1);
    return row(k+1, i, a);

def col(i, n):
    if i > n:
        return;
    row(0, i, 1);
    logging.info("");
    return col(i+1, n);

def main():
    i = 10;
    logging.info( "[INPUT] %d" % i);
    logging.info( "[OUTPUT] ");
    col(0, i);

main()
