#include <windows.h>
#include <string>
#include <cstdio>

// IDs para los botones
#define ID_BTN_INICIAR 1
#define ID_BTN_OPCIONES 2
#define ID_BTN_AJUSTES 3
#define ID_BTN_SALIR 4

// Prototipos
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
LRESULT CALLBACK ResultadoProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

// Conversión de saltos de línea
std::wstring ConvertNewlines(const std::string& input) {
    std::wstring output;
    for (char c : input) {
        if (c == '\n') output += L"\r\n";
        else output += (wchar_t)c;
    }
    return output;
}

// Ventana de resultados
LRESULT CALLBACK ResultadoProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    static HWND hwndTexto;

    switch (uMsg) {
    case WM_CREATE:
        hwndTexto = CreateWindowExW(
            WS_EX_CLIENTEDGE, L"EDIT", L"",
            WS_CHILD | WS_VISIBLE | WS_VSCROLL | ES_MULTILINE | ES_AUTOVSCROLL | ES_READONLY,
            10, 10, 560, 310,
            hwnd, (HMENU)1001, GetModuleHandleW(NULL), NULL);

        CreateWindowW(
            L"BUTTON", L"Cerrar",
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            250, 330, 100, 25,
            hwnd, (HMENU)1002, GetModuleHandleW(NULL), NULL);
        break;

    case WM_COMMAND:
        if (LOWORD(wParam) == 1002) {
            DestroyWindow(hwnd);
        }
        break;
    }

    return DefWindowProcW(hwnd, uMsg, wParam, lParam);
}

// Función principal
int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR, int nCmdShow) {
    const wchar_t CLASS_NAME[] = L"EpidecideMenu";

    HICON hIcon = (HICON)LoadImageW(NULL, L"icono.ico", IMAGE_ICON, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE);

    // Clase principal
    WNDCLASSW wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
wc.hCursor = LoadCursorW(NULL, IDC_ARROW);
    wc.hIcon = hIcon;
    RegisterClassW(&wc);

    // Clase para la ventana de resultados
    WNDCLASSW wcResultado = {};
    wcResultado.lpfnWndProc = ResultadoProc;
    wcResultado.hInstance = hInstance;
    wcResultado.lpszClassName = L"ResultadoVentana";
    wcResultado.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wcResultado.hCursor = LoadCursorW(NULL, IDC_ARROW);
    RegisterClassW(&wcResultado);

    HWND hwnd = CreateWindowExW(
        0,
        CLASS_NAME,
        L"Epidecide",
        WS_OVERLAPPEDWINDOW ^ WS_MAXIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 300,
        nullptr, nullptr, hInstance, nullptr);

    if (!hwnd) return 0;

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    MSG msg = {};
    while (GetMessageW(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessageW(&msg);
    }

    return 0;
}

// Proceso de ventana principal
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    static HWND hBtnIniciar, hBtnOpciones, hBtnAjustes, hBtnSalir;

    switch (uMsg) {
    case WM_CREATE:
        hBtnIniciar = CreateWindowW(L"BUTTON", L"Iniciar",
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            130, 50, 120, 30,
            hwnd, (HMENU)ID_BTN_INICIAR, NULL, NULL);

        hBtnOpciones = CreateWindowW(L"BUTTON", L"Opciones",
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            130, 90, 120, 30,
            hwnd, (HMENU)ID_BTN_OPCIONES, NULL, NULL);

        hBtnAjustes = CreateWindowW(L"BUTTON", L"Ajustes",
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            130, 130, 120, 30,
            hwnd, (HMENU)ID_BTN_AJUSTES, NULL, NULL);

        hBtnSalir = CreateWindowW(L"BUTTON", L"Salir",
            WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
            130, 170, 120, 30,
            hwnd, (HMENU)ID_BTN_SALIR, NULL, NULL);
        return 0;

    case WM_COMMAND:
        switch (LOWORD(wParam)) {
        case ID_BTN_INICIAR: {
            FILE* pipe = _popen("python \"C:\\Users\\NINIT\\Desktop\\EpiDecide\\main.py\"", "r");
            if (!pipe) {
                MessageBoxW(hwnd, L"No se pudo ejecutar main.py", L"Error", MB_OK | MB_ICONERROR);
                break;
            }

            char buffer[256];
            std::string output;
            while (fgets(buffer, sizeof(buffer), pipe)) {
                output += buffer;
            }
            _pclose(pipe);

            std::wstring formattedOutput = ConvertNewlines(output);

            HWND hwndResultado = CreateWindowExW(
                WS_EX_CLIENTEDGE, L"ResultadoVentana", L"Resultado de la simulación",
                WS_OVERLAPPEDWINDOW | WS_VISIBLE,
                CW_USEDEFAULT, CW_USEDEFAULT, 600, 400,
                hwnd, NULL, GetModuleHandleW(NULL), NULL);

            ShowWindow(hwndResultado, SW_SHOW);
            UpdateWindow(hwndResultado);
            Sleep(100); // sincronización

            HWND hwndTexto = GetDlgItem(hwndResultado, 1001);
            if (hwndTexto) {
                SetWindowTextW(hwndTexto, formattedOutput.c_str());
            } else {
                MessageBoxW(hwnd, L"No se pudo encontrar el área de texto.", L"Error", MB_OK | MB_ICONERROR);
            }

            break;
        }

        case ID_BTN_OPCIONES:
            MessageBoxW(hwnd, L"Opciones presionado", L"Acción", MB_OK);
            break;
        case ID_BTN_AJUSTES:
            MessageBoxW(hwnd, L"Ajustes presionado", L"Acción", MB_OK);
            break;
        case ID_BTN_SALIR:
            PostQuitMessage(0);
            break;
        }
        return 0;

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }

    return DefWindowProcW(hwnd, uMsg, wParam, lParam);
}
