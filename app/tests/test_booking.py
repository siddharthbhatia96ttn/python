def test_double_booking(client, auth_headers):
    r1 = client.post("/appointments", json={
        "doctor_id": 1,
        "start_time": "2025-01-01T10:00",
        "end_time": "2025-01-01T10:30"
    }, headers=auth_headers)

    r2 = client.post("/appointments", json={
        "doctor_id": 1,
        "start_time": "2025-01-01T10:00",
        "end_time": "2025-01-01T10:30"
    }, headers=auth_headers)

    assert r2.status_code == 400
