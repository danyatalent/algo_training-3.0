#include <iostream>
#include <array>

int main()
{
    int m(0), n(0);
    std::cin >> m >> n;
    const int N_SIZE = 1001;
    int ans = 0;
    std::array< std::pair<int, int>, N_SIZE> sectors;
    for (int i = 0; i < n; i ++) {
        int a(0), b(0);
        std::cin >> a >> b;
        std::pair <int, int> sector = std::make_pair(a, b);
        sectors[i] = sector;
    }
    for (int i = 0; i < n; i++) {
        bool survived = true;
        for (int j = i + 1; j < n; j++) {
            if ((sectors[i].second >= sectors[j].first && sectors[i].second <= sectors[j].second) || (sectors[i].first <= sectors[j].second && sectors[i].first >= sectors[j].first) || (sectors[j].first >= sectors[i].first && sectors[j].second <= sectors[i].second)) {
                survived = false;
                break;
            }
        }
        if (survived) ans += 1;
    }
    std::cout << ans << std::endl;
}