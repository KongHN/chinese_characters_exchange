%% 图片切割和交换程序
% 直接在代码里指定输入和输出路径（修改为你的实际路径）
INPUT_DIR = 'F:\科研\06Machine Learning, EEG, and Word Reading in Children\Real characters\objects real 2\objects real 2';
OUTPUT_DIR = 'C:\Users\孔昊男\Desktop\000000';

% 显示当前使用的路径
fprintf('输入目录: %s\n', INPUT_DIR);
fprintf('输出目录: %s\n', OUTPUT_DIR);

% 确保输出目录存在
try
    if ~exist(OUTPUT_DIR, 'dir')
        mkdir(OUTPUT_DIR);
    end
    fprintf('输出目录已准备好: %s\n', OUTPUT_DIR);
catch e
    fprintf('创建输出目录时出错: %s\n', e.message);
    fprintf('请检查路径: %s\n', OUTPUT_DIR);
    return;
end

% 获取所有BMP文件
try
    fileList = dir(fullfile(INPUT_DIR, '*.bmp'));
    if isempty(fileList)
        fileList = dir(fullfile(INPUT_DIR, '*.BMP')); % 处理大写扩展名
    end
catch e
    fprintf('读取输入目录时出错: %s\n', e.message);
    fprintf('请检查路径: %s\n', INPUT_DIR);
    return;
end

if isempty(fileList)
    fprintf('在目录 %s 中未找到BMP文件\n', INPUT_DIR);
    return;
end

% 处理每个BMP文件
for i = 1:length(fileList)
    % 将filename转换为字符串类型
    filename = char(fileList(i).name);
    inputPath = fullfile(INPUT_DIR, filename);
    
    try
        % 读取图片
        img = imread(inputPath);
        [height, width, ~] = size(img);
        
        % 执行横向切割和交换
        [~, baseName, ~] = fileparts(filename); % 提取不带扩展名的文件名
        outputFilename = [baseName '_horizontal.bmp'];
        outputPath = fullfile(OUTPUT_DIR, outputFilename);
        
        halfHeight = floor(height / 2);
        topHalf = img(1:halfHeight, :, :);
        bottomHalf = img(halfHeight+1:end, :, :);
        
        newImg = cat(1, bottomHalf, topHalf);
        imwrite(newImg, outputPath);
        fprintf('已处理: %s -> %s\n', filename, outputFilename);
        
        % 执行纵向切割和交换
        outputFilename = [baseName '_vertical.bmp'];
        outputPath = fullfile(OUTPUT_DIR, outputFilename);
        
        halfWidth = floor(width / 2);
        leftHalf = img(:, 1:halfWidth, :);
        rightHalf = img(:, halfWidth+1:end, :);
        
        newImg = cat(2, rightHalf, leftHalf);
        imwrite(newImg, outputPath);
        fprintf('已处理: %s -> %s\n', filename, outputFilename);
        
    catch e
        fprintf('处理文件 %s 时出错: %s\n', filename, e.message);
    end
end