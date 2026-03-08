bool isMatch(char* s, char* p) {
    char *sptr = s, *pptr = p, *sstar = NULL, *pstar = NULL;
    while (*sptr) {
        if (*pptr == '?' || *sptr == *pptr) { sptr++; pptr++; }
        else if (*pptr == '*') { pstar = pptr++; sstar = sptr; }
        else if (pstar) { pptr = pstar + 1; sptr = ++sstar; }
        else return false;
    }
    while (*pptr == '*') pptr++;
    return !*pptr;
}

