from read_data import read_data

df = read_data()

approved = df.query("Beslut == 'Beviljad'")
num_approved = len(approved)
total_approved = len(df)
approved_procent = f"{num_approved / total_approved*100:.1f}%"

def provider_kpis(provider):
    applied = df.query(f"`Utbildningsanordnare administrativ enhet` == '{provider}'")
    applications = len(applied)
    approved_applications = len(applied.query("Beslut == 'Beviljad'"))

    return applications, approved_applications
