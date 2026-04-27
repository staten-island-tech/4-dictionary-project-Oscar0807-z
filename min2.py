wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}
staff = {}
for dept, docs in wards.items():
    for doc in docs:
        if doc not in staff:
            staff[doc] = []
        else:
            staff[doc].append(dept)
print(staff)