@echo off
setlocal

rem Определяем путь к текущему скрипту и файлу afrika_dawn.mod
set "CurrentDirectory=%~dp0"
set "ModFile=%CurrentDirectory%afrika_dawn.mod"
set "ModFolder=%CurrentDirectory%afrika_dawn"

rem Убедимся, что папка существует
if not exist "%ModFolder%" (
    echo Папка %ModFolder% не существует.
    exit /b 1
)

rem Проверяем, существует ли файл afrika_dawn.mod
if not exist "%ModFile%" (
    echo Файл %ModFile% не найден.
    exit /b 1
)

rem Запускаем PowerShell для редактирования файла
powershell -Command ^
    "(Get-Content -Raw -Path '%ModFile%') -replace 'path=\"path\"', 'path=\"%ModFolder:\=/%\"' | Set-Content -Path '%ModFile%'"

echo Файл %ModFile% успешно обновлен.
