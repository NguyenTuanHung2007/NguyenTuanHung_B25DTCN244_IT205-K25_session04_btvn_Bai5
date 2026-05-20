total_revenue = 0
total_count = 0
large_count = 0
choice = 'C'

while choice.upper() == 'C':
    total_count += 1
    val = int(input(f'Khách hàng {total_count} - Nhập giá trị hóa đơn: '))
    
    total_revenue += val
    if val >= 1000000:
        large_count += 1
        
    choice = input('Có muốn nhập tiếp không? (C/K): ')

print('\n--- Báo cáo doan thu cuối ngày ---')

if total_count > 0:
    ratio = (large_count / total_count) * 100
    print(f'Tổng số hóa đơn đã xử lý: {total_count} hóa đơn')
    print(f'Tổng doanh thu ngày hôm nay: {total_revenue:,} VND')
    print(f'Số hóa đơn lớn (>= 1,000,000 VND): {large_count} hóa đơn')
    print(f'Tỷ lệ hóa đơn lớn đạt: {ratio:.1f}% trên tổng số đơn hàng')
else:
    print('Hệ thống chưa ghi nhận hóa đơn nào trong ca làm việc')