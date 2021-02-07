from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'test':
        counter_click[from_landing] += 1
        print(counter_click)

    elif from_landing == 'original':
        counter_click[from_landing] += 1
        print(counter_click)
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render(request, 'index.html', context={'counter_click': counter_click[from_landing]})


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'test':
        counter_show[ab_test_arg] += 1
        return render(request, 'landing_alternate.html')
    elif ab_test_arg == 'origin':
        counter_show[ab_test_arg] += 1
        return render(request, 'landing.html')
    return render(request, 'index.html')
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # return render(request, 'landing.html')


def stats(request):
    origin = counter_click['original']/counter_show['origin']
    test = counter_click['test']/counter_show['test']
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': test,
        'original_conversion': origin,
    })
