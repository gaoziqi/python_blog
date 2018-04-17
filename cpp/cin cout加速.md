# cin cout加速
    static auto x = [](){
        std::ios::sync_with_stdio(false);
        std::cin.tie(0);
        return 0;
    }();