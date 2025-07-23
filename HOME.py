<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/react@18.2.0/umd/react.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@18.2.0/umd/react-dom.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@babel/standalone@7.22.9/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    // Komponen Card untuk statistik
    function StatCard({ title, value, icon }) {
      return (
        <div className="bg-white p-6 rounded-lg shadow-md flex items-center space-x-4">
          <div className="text-3xl">{icon}</div>
          <div>
            <h3 className="text-gray-500 text-sm font-medium">{title}</h3>
            <p className="text-2xl font-semibold">{value}</p>
          </div>
        </div>
      );
    }

    // Komponen untuk grafik
    function ChartCard() {
      React.useEffect(() => {
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
              label: 'Penjualan',
              data: [12, 19, 3, 5, 2, 3],
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1
            }]
          },
          options: {
            responsive: true,
            scales: {
              y: { beginAtZero: true }
            }
          }
        });
      }, []);

      return (
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold mb-4">Grafik Penjualan</h2>
          <canvas id="myChart"></canvas>
        </div>
      );
    }

    // Komponen untuk daftar aktivitas
    function ActivityList() {
      const activities = [
        { id: 1, desc: "Pesanan baru #1234", time: "10 menit lalu" },
        { id: 2, desc: "Pembayaran diterima dari John Doe", time: "1 jam lalu" },
        { id: 3, desc: "Produk baru ditambahkan", time: "2 jam lalu" },
      ];

      return (
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-lg font-semibold mb-4">Aktivitas Terbaru</h2>
          <ul className="space-y-4">
            {activities.map((activity) => (
              <li key={activity.id} className="flex justify-between">
                <span>{activity.desc}</span>
                <span className="text-gray-500">{activity.time}</span>
              </li>
            ))}
          </ul>
        </div>
      );
    }

    // Komponen utama Dashboard
    function Dashboard() {
      return (
        <div className="min-h-screen bg-gray-100 p-6">
          <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <StatCard title="Total Pengguna" value="1,234" icon="👥" />
            <StatCard title="Penjualan Bulan Ini" value="$5,678" icon="💰" />
            <StatCard title="Pesanan Baru" value="89" icon="📦" />
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <ChartCard />
            <ActivityList />
          </div>
        </div>
      );
    }

    // Render aplikasi
    ReactDOM.render(<Dashboard />, document.getElementById('root'));
  </script>
</body>
</html>