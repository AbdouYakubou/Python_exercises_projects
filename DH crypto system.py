import random

def diffie_hellman():
    # number (p) which is also the size and generator (g) shared by both parties
    p = 23  # Size
    g = 5   # generator

    print(f"Public parameters: p = {p}, g = {g}")

    #Let both party be A and B respectively, Each party chooses a private key
    private_key_A = random.randint(1, p-1)
    private_key_B = random.randint(1, p-1)

    print(f"Private key of Party A: {private_key_A}")
    print(f"Private key of Party B: {private_key_B}")

    # Computing the public keys
    public_key_A = pow(g, private_key_A, p)
    public_key_B = pow(g, private_key_B, p)

    print(f"Public key of Party A: {public_key_A}")
    print(f"Public key of Party B: {public_key_B}")

    # Exchanging public keys and computing the shared secret
    shared_secret_A = pow(public_key_B, private_key_A, p)
    shared_secret_B = pow(public_key_A, private_key_B, p)

    print(f"Shared secret calculated by Party A: {shared_secret_A}")
    print(f"Shared secret calculated by Party B: {shared_secret_B}")

    # Verifying that both parties have the same shared secret
    assert shared_secret_A == shared_secret_B, "Shared secrets do not match!"
    print("Shared secret exchange successful!")

if __name__ == "__main__":
    diffie_hellman()