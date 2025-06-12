#include <windows.h>

// IDs para los botones
#define ID_BTN_INICIAR 1
#define ID_BTN_OPCIONES 2
#define ID_BTN_AJUSTES 3
#define ID_BTN_SALIR 4

// Prototipo del callback
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

// Función principal
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, LPSTR, int nCmdShow) {
    const char CLASS_NAME[] = "EpidecideMenu";

    // Registrar clase de ventana
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    RegisterClass(&wc);

    // Crear ventana
    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        "Epidecide",
        WS_OVERLAPPEDWINDOW ^ WS_MAXIMIZEBOX, // sin botón de maximizar
        CW_USEDEFAULT, CW_USEDEFAULT, 400, 300,
        nullptr, nullptr, hInstance, nullptr
    );

    if (!hwnd) return 0;

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    // Loop de mensajes
    MSG msg = {};
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

// Función de proceso de ventana
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    static HWND hBtnIniciar, hBtnOpciones, hBtnAjustes, hBtnSalir;

    switch (uMsg) {
        case WM_CREATE:
            // Crear botones
            hBtnIniciar = CreateWindow("BUTTON", "Iniciar",
                WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
                130, 50, 120, 30,
                hwnd, (HMENU)ID_BTN_INICIAR, NULL, NULL);

            hBtnOpciones = CreateWindow("BUTTON", "Opciones",
                WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
                130, 90, 120, 30,
                hwnd, (HMENU)ID_BTN_OPCIONES, NULL, NULL);

            hBtnAjustes = CreateWindow("BUTTON", "Ajustes",
                WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
                130, 130, 120, 30,
                hwnd, (HMENU)ID_BTN_AJUSTES, NULL, NULL);

            hBtnSalir = CreateWindow("BUTTON", "Salir",
                WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
                130, 170, 120, 30,
                hwnd, (HMENU)ID_BTN_SALIR, NULL, NULL);
            return 0;

        case WM_COMMAND:
            switch (LOWORD(wParam)) {
                case ID_BTN_INICIAR:
                    MessageBox(hwnd, "Iniciar presionado", "Acción", MB_OK);
                    break;
                case ID_BTN_OPCIONES:
                    MessageBox(hwnd, "Opciones presionado", "Acción", MB_OK);
                    break;
                case ID_BTN_AJUSTES:
                    MessageBox(hwnd, "Ajustes presionado", "Acción", MB_OK);
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
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
