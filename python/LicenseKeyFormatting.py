def licenseKeyFormatting(S: str, K: int) -> str:
    if K == 0:
        return S
    S = (S.replace("-", "")).upper()
    mod = len(S) % K
    if mod == 0:
        return '-'.join([S[i:i + K] for i in range(0, len(S), K)])
    else:
        return '-'.join([S[0:mod]] + [S[i + mod: i + mod + K] for i in range(0, len(S)-mod, K)])
